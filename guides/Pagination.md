# Step 1 - Create a project
At this point you're ready to build your new project.

To remind you, our mission is to implement a simple *Contact service* that will allow managing contacts.

## In this topic you will: 
* [Cloning the repo](#cloning-the-wix-academy-repository)
* [Generating a server project using the wix-wnp-cruderator tool](#generating-a-server-project-using-wixwix-wnp-cruderator)
* [Building the generated skeleton](#skeleton-build)
* [Overview the generated skeleton](#skeleton-overview)
* [Updating API](#update-api)
* [Implementing service (in-memory)](#implement-service)
* [Adding database integration](#add-db)

## Cloning the `wix-academy` repository <a name="clone-repo"></a>
You will build the new project and eventually push it to `github`. 
All the Node _something-to-prod_ projects should be stored under [node-something-to-prod-projects](../../node-something-to-prod-projects) folder.
So we are going to clone the `wix-academy` repository, create a new branch, and you will generate your new project there.

1. In terminal from the folder that will hold your projects, run `git clone git@github.com:wix-private/wix-academy.git`. It will clone the repository to your computer.
2. Go to the `wix-academy` folder and create a new branch - run `git checkout -b YOUR-NAME-something-to-prod`

You are now ready to generate your new project there.

## Generating a server project using [@wix/wix-wnp-cruderator](https://github.com/wix-platform/wix-node-platform/tree/master/cruderator/wix-wnp-cruderator)
When you have done the [Creating a node or client-side project](https://github.com/wix-private/fed-handbook/blob/master/ZERO_TO_PRODUCTION.md) task, you have used `yoshi` to generate an empty project.<br/>
Now we will use a **different tool** to generate a service skeleton - `@wix/wix-wnp-cruderator` (not `yoshi`). <br/>
`@wix/wix-wnp-cruderator` is suitable for bootstrapping **server-side** apps exposing platformized API (services).       

In terminal go to the folder you cloned the _wix-academy_ repository to - to the `wix-academy/server-onboarding/node-something-to-prod-projects` folder, 
and run the following command under it (_it might take some time for this tool to start when running via `npx` as it have some dependencies that should be fetched too_):

```shell script
npx @wix/wix-wnp-cruderator
```     

Follow the wizard. In particular, fill these fields in the following way: 
 - module name: `[YOUR NAME]-node-something-to-prod` (we have a lot of developers - so would check first, that a project with the such name does not exist in this folder)
 - company name: `examples`
 - entity: `contact`

### What just happened here? 
Running this command created a [lerna.js](https://lerna.js.org/) managed monorepo with two modules (under the `packages` folder):
- API with Protobuf & documentation (under `packages/node-something-to-prod-[YOU NAME]-api`)
- Bootstrap server that implements the API  (under `packages/node-something-to-prod-[YOU NAME]-server`)

This is just a **skeleton** with a sample API definition and implementation that we will change to implement our service.

#### Monorepo
You are probably familiar with this term but basically it means a singe code repository containing several modules. 
This is the way most of the project at Wix are organized. When working with monorepos, the development process depends a lot on the stack you are using. 
For any stack, the very basic and clear need is to be able to change few modules locally and make all the local modules to be aware of those changes.
  
For the Node projects the basic way to do it is to use the `npm link` command, but it is quite inconvenient for any real world repository. 
There are several solutions available to deal with it - [lerna.js](https://lerna.js.org/), [yarn workspaces](https://classic.yarnpkg.com/en/docs/workspaces/), [rush](https://rushjs.io/). 
In this project we will use `lerna`, but you might meet usages of other tools at Wix as well.

You can learn about `lerna` in the provided above link, but for now we need to know few basics.  
- `lerna.json` - the configuration file defining `lerna`'s behaviour, specifically - what modules (_packages_) should be "linked". Located in the repository's root.
- [lerna bootstrap](https://github.com/lerna/lerna/tree/main/commands/bootstrap#readme) - the main `lerna` command - it installs the dependencies for all the relevant modules, and apply the linkage between them
- [lerna add](https://github.com/lerna/lerna/tree/main/commands/add#readme) - adds a dependency to the package(s) mainained by `lerna` 

Normally you would need to install `lerna` globally, but we can run it via `npx` - like `npx lerna add ...`.

#### Dockerfile
Almost all the applications in Wix are running in the Kubernetes environment, that is, an application runs inside a docker container on the Kubernetes pod. In order to allow creating such a container, we need to have an application's docker image. Such image is built by the CI system during the application's build process. Every deployable Node application must have a `Dockerfile` in the root level. The application you generated has such a file under the **server** module (`/packages/[YOUR NAME]-node-something-to-prod-server`) - you can inspect it and see that it has a single line - basically it inherits from a base docker image maintained by Node Platform that has all the logic of packing applictions code into the docker image.

Currently, the Node Platform supports 2 base docker images:
 - `docker-repo.wixpress.com/wix-bootstrap-monorepo:stable` - for the applications built in [Falcon CI](https://falcon.dev.wixpress.com) as monorepo-based. 
 - `docker-repo.wixpress.com/wix-bootstrap-onbuild:stable` - for applications built in [old TC CI](https://tc.dev.wixpress.com/) as an individual applications.

Eventually, all the application will migrate to Falcon. But for simplicity reasons currently the project you are going to create will be automatically built in the [old TC CI](https://tc.dev.wixpress.com/project.html?projectId=wix_academy_ServerOnboarding_NodeSomethingToProdProjects) thus we need to change the base image we inherit from to the "old" one.

**ACTION REQUIRED!** Open the `Dockerfile` located in the root of the the **server** module (`/packages/[YOUR NAME]-node-something-to-prod-server`) and replace its content with the following:

```
FROM docker-repo.wixpress.com/wix-bootstrap-onbuild:stable
```

This has no effect on the local development process but it will allow the old TC CI to create a correct image for your app once we will get there.

#### Lock files
In a real production project you will probably have and maintain package manager lock files - such as [package-lock.json](https://docs.npmjs.com/cli/v7/configuring-npm/package-lock-json) or [yarn.lock](https://classic.yarnpkg.com/en/docs/yarn-lock/) - depending on what package manager is in use (`npm`/`yarn`). 
The idea of the lock files is simple - to freeze the version of the dependencies so every time you do `npm install` you would get the exact same dependencies. 

Node Platform has a lot of small libraries (npm modules), but due to historical reasons and the maintenance complexity the whole state of the `master` branch is considered as a current version of the Node Platform. That is, Node Platform does not provide any guarantees on interoperability between "different" versions of its modules. To align the version to the current state, one could run `npx @wix/wix-wnp-version --fix --current` command in the app folder, that would update the `package.json` file with the relevant versions. Having lock files requires updating those files as well which is not necessarily simple.

To properly maintain the lock files, the Wix internal [Loki](https://github.com/wix-private/loki#loki) utility should be used. It is enabled by default in the project you have just generated - you can inspect the main `package.json` file and file the `loki` definition there. But updates of Loki are CI events based and do not happen immediately/online. So for the purpose of this task we would disable using lock files for a sake of simplicity.

**ACTION REQUIRED!** In the root folder and in both package folders - `/packages/[YOUR NAME]-node-something-to-prod-server` and `/packages/[YOUR NAME]-node-something-to-prod-api` do the following:
  1. Create/update the `.npmrc` file with to have this line in it:
     ```
     package-lock=false
     ```
  2. Create/update `.gitignore` file with to have this line in it:
     ```
     package-lock.json
     ```

### Building and testing the project <a name="skeleton-build"></a>
Now we have a service skeleton, let's make sure it is all good and ready. First of all, let's install dependencies.

Go to the terminal and run this command in your module's root (`[YOUR NAME]-node-something-to-prod`):
```shell script
npm install
``` 

It will install `lerna` and run the `lerna bootstrap` command (it is set as a `postinstall` action in the package.json).

Wait for that command to complete and then go to the **server** module (`/packages/[YOUR NAME]-node-something-to-prod-server`) and run
```shell script
 npm run build
``` 

This command builds your project - that includes:
 - generating code from the proto files 
 - transpiling your typescript code into javascript

**IMPORTANT:** Remember to run this command each time you do any changes to your proto!

Now run the following command to execute the tests:
```shell script
 npm test
``` 

You should see that a single test we have, passed:

![empty-project-test](../images/step1-test-skeleton.png) 

We can now open the project in IntelliJ (or other IDE of your choice) and get to the real work! 
> In IntelliJ just open the root level module (`[YOUR NAME]-node-something-to-prod`) as a project.

![empty-project](../images/step1-initial-project-view.png) 

### Code names 
From now on let's call the `packages/node-something-to-prod-[YOU NAME]-api` module an "_**API module**_", 
and the `packages/node-something-to-prod-[YOU NAME]-server` module - a "_**Server module**_".

### Skeleton overview <a name="skeleton-overview"></a>
We have this sample service ready and working. You will need to change it to implement our real service methods. In order to do so, you should understand the code structure. 
Basically, the main high-level blocks for any platformized service implementation would be:
 - API definitions (proto)
   - What capabilities your service will expose
 - API implementation (actual javascript/typescript code)
   - The logic implementation - how does your service do what it needs to do 
 - Binding API implementation to the bootstrap app (via `.service()` in `index.ts`)
   - Making your API available to be called form outside (via RPC/REST)
 - Tests of the API implementation - including 
   - test environment configuration
   - test code
      

#### Let's overview the main parts in more detail:
 - **_API module_** contains the definitions of the API in a proto format.  
    - We use Protocol Buffers files to define our APIs so that they can be language-agnostic. In order to work with the defined APIs, 
      we need to convert the proto definitions into a specific language code.
      
      Within Node Platform we have [@wix/wix-proto-codegen](https://github.com/wix-platform/wix-node-platform/tree/master/rpc/wix-proto-codegen#wix-proto-codegen) tool for that (we will use it soon). 
      This tool generates javascript and typescript (DTOs and interfaces) code from the proto files. 
      The generated code can then be used in our Node application to implement the API (service), and in client apps that consume our API.
      Using proto files is part of our platformization effort. <br/>
      To understand more about proto, you can read [Google's documentation](https://developers.google.com/protocol-buffers/docs/proto3)
      and our [Wix proto guideline](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/protobuf)
      
      In Node projects, the API should be defined in a separate module because of the way the proto magic works - thus this structure. 
      
    - In this case APIs are defined in `src/main/proto/com/wix/examples/contact_api.proto` file in the _API module_. 
      Note the folders structure - it should match the `package` definition in the proto file.  
    
    - API must be documented. Learn more about this in the [Documentation section](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/documenting-your-api#platformization-guidelines_documenting-your-api_documentation) of the Platformization Guidelines.
      `src/main/proto/documentation.yaml` is a mandatory part of the documentation and must exist in every API module.
    
    - Let's take a look at `package.json` file. Important parts here:
      - API modules are marked with `"wnp_type": "proto"` property
      - API module must have [@wix/wix-proto-module-validator](https://github.com/wix-platform/wix-node-platform/tree/master/rpc/wix-proto-module-validator#wix-proto-module-validator) dependency
        and `wix-proto-module-validator` as a test script. That library checks that all the proto definitions are correct. When you will update the API, run `npm test` in the _API module_ to validate your changes.   
      
 - **_Server module_** is a Node _bootstrap_ app that contains the API implementations and exposes the relevant endpoints, so the API could be consumed from outside.
    - `src/services/ContactServiceImpl.ts` contains the [implementation](https://github.com/wix-platform/wix-node-platform/blob/master/bootstrap/docs/rpc-server.md#implementing-service-logic) of the sample service. Go ahead and take a look. You will find out that `ContactServiceImpl` extends `services.com.wix.examples.ContactService`.
      What's that `ContactService`? That is the class generated out of proto definitions by `wix-proto-codegen` tool!
      
    - When we want to make server-to-server calls (from another service to ours) we use technology called [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call). 
      In Wix RPC calls (server and client) are facilitated by Node Platform (Framework), which generates stubs for client and server.
      We need to expose our API as an RPC service. You can find the node RPC server guide [here](https://github.com/wix-platform/wix-node-platform/blob/master/bootstrap/docs/rpc-server.md).<br/>
      The `index.ts` file contains the [binding](https://github.com/wix-platform/wix-node-platform/blob/master/bootstrap/docs/rpc-server.md#binding-implementation-onto-bootstrap-app) of the implementation to the bootstrap app - the `.service(ctx => new ContactServiceImpl(ctx))` part. It instructs the Node Platform code
      that `ContactServiceImpl` is a platformized service, and it should be loaded and exposed via RPC and REST (if any REST exposure are defined in the proto).
      
    - Let's take a look at the (single) method signature - `sayHello(aspects: AspectStore, req: requests.com.wix.examples.SayHelloRequest)`
      - The first argument is `aspects` - - you can read about it [here](https://github.com/wix-platform/wix-node-platform/tree/master/aspects#aspects)
      - The second one is an instance of a class `SayHelloRequest` - generated out of the proto definitions and having all the properties defined in proto
      
    - In order to [test](https://github.com/wix-platform/wix-node-platform/blob/master/bootstrap/docs/rpc-server.md#testing) the service, we have the `__tests__/server.it.ts` file with a single test
      that creates a test environment using [TestEnv](https://github.com/wix-platform/wix-node-platform/tree/master/testing/wix-test-env#wix-test-env), starts it (including our app) 
      and testing the service by sending an actual gRpc request to it. Note that we use [Jest](https://jestjs.io/) testing framework here.
      - You can/should read about `TestEnv` in the provided link but let's discuss these important points:
        - `withCollaborators` obviously takes care of app's collaborators but what are those? Technically - a collaborator will be an instance of some testkit. 
          Logically - it represents some external dependency of your app, like a database, Redis, or some other service. In production environment your application assumes 
          that those dependencies are available and just tries to communicate with them. In test environment you should provide _simplicators_ that will represent those dependencies. 
          For example, your application works with Mysql. In production DBAs and System teams are taking care of a database availability. But when you run your IT test, your app's code
          will do what it's meant to do - will try to connect to some database (using the real protocol - it's IT test, right?). So in order to allow this code to work we need to provide
          a database to be available for tests. For Mysql we will have a Mysql testkit, that will start a local instance of a database (maybe inside a docker container) - and
          the app will talk to it when running the tests. <br/>
          Collaborators should be available **before** the app is starting - because the app might need to communicate with them (like connect to a database) on the startup. 
          Thus, it is important to start the collaborators and the application in the correct order. `TestEnv` takes care of it.
        - `withMainApp` - this is most basic part - you just tell the `TestEnv` where is the entry point file of your application
        - `withGrpcClients` - in IT tests you will want to test your service via real RPC protocol. gRpc is the default one in Wix. To call some endpoint via gRpc protocol
          you will need a _gRpc client_ taht is aware of a proto definitions of the service and the server address (your app in this case). This `withGrpcClients` helper method
          generates a gRpc client that is pre-configured with the address of the started application.
        - `beforeAndAfter()` - helper that takes care of starting the whole environment before the tests execution and to stop it after the tests execution. 
          There is this `beforeAndAfterEach()` alternative - it will start/stop the environment per test (so each test will get a very new enviroment state) but in IT tests it's
          usually too expensive - and normally `beforeAndAfter()` is used.            
        
      - You can see in the test that we create aspects for test purposes using `apiGwTestkit.callContextBuilder()` - this is suitable 
        when we need to pass some identity-related data (as we do in the skeleton test). 
      - For more simple cases, when we just need an instance of aspects with a generic data, Node Platform provides [@wix/wix-aspects-testkit](https://github.com/wix-platform/wix-node-platform/tree/master/testing/wix-aspects-testkit#wix-aspects-testkit)
        that can generate a valid aspects for tests - you can use it when you will add you tests.  
      
    - *_You might note that we have another collaborator and plugin for working with it in the skeleton - `API Gateway client`. We will get to it later._  
            
    
### Hints
Now when you understand the structure of the skeleton, you can start actually changing it and implementing our real service. Few tips to help you on your way:

- You can add new methods to the service without touching/removing the sample one at the beginning, so you will have a working example
 
- You will need to install missing dependencies in the project. Here are few examples of the commands to do that (to be executed from the project's root folder):
    ```shell script
    # Installs lib@1.0.0 as a dev dependency of node-something-to-prod-solution-api
    npx lerna add lib@1.0.0 packages/node-something-to-prod-solution-api --dev
        
    # Installs lib@1.0.0 as a production dependency of node-something-to-prod-solution-server
    npx lerna add lib@1.0.0 packages/node-something-to-prod-solution-server    
    ```
    
    Alternatively, you can manually update the `package.json` file(s) with the desired dependencies and just run the 
    following command in the root module to apply all the changes at once: 
    ```shell script
    npm lerna bootstrap
    ```
 - Your are working on a branch of a github `wix-academy` repo - you might want to commit your changes periodically so you 
   will have clean working state between different steps.
   
 - When you will run the `npm run build` or `npm test` command in the _Server module_, it will transpile the typescript code to the javascript and save it into the `dist` folder. 
   When running test with IntelliJ, it might prefer looking at `dist` for the production code - so make sure you either build your production changes before running the test or remove the `dist` folder.  

## Updating the Proto API <a name="update-api"></a>
Let's begin! For the contacts service that we are writing, we need to be able to Create / Read / Update and Delete contact. 

1. To define our API in the proto file, we need to first think what does our API include. We are creating a Contact, therefore:
   * What fields should a contact have? 
   * What type are the fields? 
   * Are any of them mandatory?
2. We want to start simple - so let's keep these properties for a contact for now - `id`, `name`, and `description`. 
3. Open the **contact-api.proto** file (you will find it under **src/main/proto/com/wix/examples** folder).
   * This path is important - the proto files must be stored in the nested folders under `src/main/proto/` according to their _proto package name_ (`com.wix.examples` in our case) 
4. Declare the 4 APIs.  
   * Use our [Wix proto guideline](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/protobuf)
   * **Hint**: in the Update method you might want to accept `google.protobuf.FieldMask` to know what set of fields you should update. 
     > **Why this is important?** <br/> 
     Because with proto-based implementation a client might send only part of the properties defined in a message - all others will be assigned with the _default_ value
     according to their type. For example, any `string` property missing in the request will be assigned with an empty string value. 
     But since the client haven't actually sent this value, we don't want to update the property to have an empty string. So how would we know, what properties to update?
     The answer - according to the list of fields sent in the `FieldMask` property! <br/>
     You can read more about it in [this section](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/proto-generated-code-caveats#platformization-guidelines_proto-generated-code-caveats_partial-updates) of the guide.

     - You can use [protobuf-fieldmask](https://www.npmjs.com/package/protobuf-fieldmask) lib to apply filtering based on the field mask.

   * You can leave for now the auto-generated API (`SayHello`), but it should be eventually removed from the proto file and from the code
   * Check the API module validity after you did your changes
     * Run `npm test` command in the _API module_ - it should complete without errors  
     * **Hint**: you might need to add missing _production_ dependencies to the _API module_:
       - `@wix/protos-query`
       - `@wix/protos-common`

   [solution](../code-examples/2-proto-api.md)

## Implementing the ContactService <a name="implement-service"></a>
We have defined the API, now we can start working on the implementation.  

1. First we will need to generate a real Javascipt/Typescript code from the API proto definition. 
As we said above, Node Platform provides the [wix-proto-codegen](https://github.com/wix-platform/wix-node-platform/tree/master/rpc/wix-proto-codegen) tool to do that.
Your _Server module_ has already a dependency on it. Now we need to run it in order to generate code from the proto that you changed (it will search for all the relevant API modules among the dependencies and process them). 
We also have a dedicated npm script defined in the _Server module_'s `package.json` file - find it and run it!    

    <details><summary>Show Solution</summary>
    <pre><code>npm run clean && npm run proto</code></pre></details>

1. This is a good point to write our first real test!
Since we are practicing TDD (Test Driven Development) at Wix, we will write the tests before we actually implement the method.  
    1. Let's stop here and discuss [Testing at Wix](../explanations/testing-at-wix.md).
    
    2. Welcome back! One more thing before we get down to business: let's see what test we already have from the auto-generated skeleton. (Remember, we already ran it and it passed?) 
    Open and try running the existing test `__tests__/server.it.ts` in the _Server module_ - you would still expect it to pass, right? But it failed! 
    You get a typescript compilation error of a form<br/> _`Non-abstract class 'ContactServiceImpl' does not implement inherited abstract member 'createContact' from class 'ContactService'`_.<br/><br/>
    Why that? Indeed, we have added new methods to the proto definition of the service but haven't added any implementation yet. <br/> 
    Try to fix the _compilation_ issue - it will be totally fine to have some `Unimplemented` error thrown in a run-time instead of the compilation error. After your fix the test should pass.
    
    <details><summary>Show Solution</summary>
    <pre><code>
      async createContact(aspects: AspectStore, req: requests.com.wix.examples.CreateContactRequest): Promise<responses.com.wix.examples.CreateContactResponse> {
        throw new Error('Unimplemented');
      }
      async deleteContact(aspects: AspectStore, req: requests.com.wix.examples.DeleteContactRequest): Promise<responses.com.wix.examples.DeleteContactResponse> {
        throw new Error('Unimplemented');
      }
      async getContact(aspects: AspectStore, req: requests.com.wix.examples.GetContactRequest): Promise<responses.com.wix.examples.GetContactResponse> {
        throw new Error('Unimplemented');
      }
      async updateContact(aspects: AspectStore, req: requests.com.wix.examples.UpdateContactRequest): Promise<responses.com.wix.examples.UpdateContactResponse> {
        throw new Error('Unimplemented');
      }
    </code></pre></details>
    
    3.  Now you're ready to write your tests. Stop for a few minutes, and try to think what are the tests that you want to write for this endpoint. How do you expect it to behave? What are its expected side effects? How will you call your RPC service?    
    You can start with tests for one Api: `CreateContact`.
    
    4. Did you do some thinking? Great! The test spec that you have thought of should be added to `server.it.ts`   
    Go ahead and implement your test. Use the [RPC guide](https://github.com/wix-platform/wix-node-platform/blob/master/bootstrap/docs/rpc-server.md) to understand better how to test an RPC server.   
    Remember - we only have the default sample service implementation so far, we didn't implement the real methods yet, 
    so we want to get to a stage where we get that `Unmplemened` error you added.
       - **Hint**: you can use [@wix/wix-aspects-testkit](https://github.com/wix-platform/wix-node-platform/tree/master/testing/wix-aspects-testkit#wix-aspects-testkit) 
         to generate empty aspects (in this case it's good enough - we don't need to pass anything special via aspects when calling our service) - `aspectsBuilder().build()`.    
    
    5. When finished, you can look at the solution [here](../code-examples/2-first-test-create-contact.md).


2. Now we want to implement the `CreateContact` API real simple logic
   1. Implement the `createContact` method. In TDD we will write the smallest code that will make the test pass. Can you think what it is?
   Note: The function returns a promise. you will need to mark the function as `async` for it to work. If you're unfamiliar with ES6 async/await you can read about it [here](https://javascript.info/async-await).   
      - [solution](../code-examples/2-create-conacts-impelementation.md)
   4. Run your test and make sure it passes.

3. Continue writing tests and implementing the other CRUD API's in ContactService. 
   At this point we are OK with storing data in memory - we will switch to a database in the next step.   
       - **Hint**: we want to generate the `id` (it should be UUID - use can use `v4()` method from [uuid](https://www.npmjs.com/package/uuid) lib) in the `createContact` - we do not want to get it from the request (we will want this field to be defined as `read only` in proto later).    

4. Refactor time. Look at your test code and see if you can refactor it, make sure all the tests still pass.   
   - [solution - tests](../code-examples/2-crud-test-after-refactor.md)
   - [solution - service code](../code-examples/2-crud-service-after-refactor.md)

## Save the data in the DB <a name="add-db"></a>
We have a working service now, but the data is kept in memory and will get lost when we restart.   
We want to save the data in a DB - let's use MySql. In order to communicate with MySql from the Node bootstrap app you should use the _Mysql plugin_.

1. First of all, you can learn [here](https://github.com/wix-platform/wix-node-platform/blob/master/bootstrap/README.md#bootstrap-plugins) about Node Platform plugins.

2. Obviously, we will need to have some DAO instance in our service to store data to the DB. That DAO would need to have these: 
   - some API to allow storing data to the concrete table 
   - and to do so - an instance of Mysql client (the one you will create with the plugin's API soon). 
    
3. Let's start by creating a new `dao` folder and in it create an _empty_ `ContactsDao` class and wire it to our service. (later you will add a Mysql client there and implement the logic). 
   - Wiring means basically that we want to get an instance of the `ContactsDao` as a parameter to the `ContactServiceImpl` constructor.
   - As you can see in the `index.ts` file, the `.service()` method where the instance of our service is created, is passing the `ctx` parameter
     which is a [context](https://github.com/wix-platform/wix-node-platform/tree/master/bootstrap#bootsrap-context) returned from the `config.ts` (wired via `.config()` method). <br/>
     Config function executed once on the application's startup. It is the place to initializes your collaborators, that you want to create once and re-use all over your code - like RPC clients, 
     database clients, Greyhound (our Kafka library) producers and consumers, etc.  
   - So for starters, let's create an instance of `ContactsDao` there, put it on the context - so it will be available in the `ContactServiceImpl` constructor.
   - After you are done, run the tests to verify that everything is still compiling and working fine
   - [solution](../code-examples/2-dao-config.md)
  
4. Now let's configure our `ContactsDao` with an instance of Mysql client. To do so, we need to add 
   the [Mysql plugin](https://github.com/wix-platform/wix-node-platform/tree/master/bootstrap-plugins/mysql/wix-bootstrap-mysql#wix-bootstrap-mysql) 
   and create a client instance in the `config.ts`. 
   - Follow the plugin's documentation to do so (remember to add dependencies using `lerna`, not `npm install` directly).
   - You will need to provide the database name. Set it to `contact_us`. This name will be relevant when you will wire Mysql testkit for tests in the next step and in production later. 
   - When you are done, you can try to run the tests, but they will fail now (with an error similar to `Error: ENOENT: no such file or directory, open 'target/configs-1/wix-bootstrap-mysql.xml'`)! <br/>
     Why that? Because now on the startup your app is trying to load Mysql configuration in order to connect to the database, but you didn't prepare the test environment for that yet. It's your next step.
   - [solution](../code-examples/2-dao-config-with-mysql-client.md) 
  
5. Now we'll adjust our test environment, so we can start the app and be able to store data to the database.
   - We need a database to work with in the tests. For Mysql we have the [Mysql testkit](https://github.com/wix-platform/wix-node-platform/tree/master/testing/wix-mysql-testkit#wix-mysql-testkit), 
     that starts a docker container with a real Mysql running inside.
   - Follow the testkit's documentation and add the testkit to the environment (we are using `TestEnv` - so that's the place)
     - One of the mandatory parameters to the testkit is `schema` - basically, it's a SQL file describing the table. You need to define one - think what the table should look like. 
       Store the file under the `__tests__/schemas/contact_us.sql` (you will need to create it).<br/>
       Schemas are defined using DDL (_Data Definition Language_) - see the Mysql [CREATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-table.html) syntax for a reference.
     - Also, you need to pass the database name you picked when initialized the Mysql client in `config.ts` - the `contact_us`.
     - **Hint**: as we said, the Mysql testkit is dockerized. Usually, it might take a while to start such a testkit as starting a docker container is an expensive operation. 
       You might want to tune the tests timeout - you can do it by changing the `testTimeout` property in the `package.json` file (60000 ms should be enough).
   - Once you are done - run the tests. Now they should pass - as the environment is ready, and the production code has a database to connect. (But remember - we still didn't implement the DAO logic)
   - [solution](../code-examples/2-mysql-test-config.md)
   
6. OK, so now we have everything wired and ready to implement the `ContactsDao`, to use it for real in the `ContactServiceImpl`, and to remove the in-memory storage.
   - Think what API the DAO should expose. Implement it - use the [Mysql plugin docs](https://github.com/wix-platform/wix-node-platform/tree/master/bootstrap-plugins/mysql/wix-bootstrap-mysql#wix-bootstrap-mysql)
     - **Hint**: you need to add `@wix/wix-bootstrap-mysql` to your production dependencies of the _Server module_
     - **Hint**: you might want to use Mysql client's `queryPromise` method
   - Once you are done - run the tests and verify that they are still green.
   - [solution](../code-examples/2-contact-dao-implementation.md)

7. Now let's make sure your code is not only correct and tests are passing but also that the linter is happy. For that we will run `npm test` command in the _Server module_.
   It will run the test and also the lint check which is defined as a `posttest` [script](https://docs.npmjs.com/cli/v6/using-npm/scripts) in `package.json`.
   - go to a terminal to the _Server module_ and run `npm test` command
   - make sure everything passes OK  

### Clean up
If you haven't done it yet, it could be a good time to get rid of the sample API generated by the `wix-wnp-cruderator` - the `SayHello` method. Remove the code related to it:
 - from the proto
 - from the service implementation
 - from the tests
 
**Hint:** _we will add an integration with API Gateway client in the following steps, so you can leave the dependency on `@wix/wix-bootstrap-api-gw-client`, loading it as a plugin and adding to the context._
 
### Where to go next?
[Get the code to production](2-get-code-to-production.md)
