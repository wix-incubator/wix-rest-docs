# Step 4 - Implement the endpoints

## What your service currently has
* All tests (ITs and E2Es) are green.
* A Loom `<your-name>-something-to-prod` service, deployed on 2 instances on DC 42.
* All instances are up and pass health tests.
* Your service exposes a proto based API for CRUD operations of a `ContactForm` entity. You can examine the API in the `contact_us.proto` file. The API implementation is in the `ContactUsImpl` Scala class.
* You are able to issue successful requests to your service via Fire Console.

## Your mission in this step
We want to expand the `ContactForm` entity to contain more information about a contact.<br>
Currently the only information a `ContactForm` has are the following properties: `id`, `name` and a `description`. This is not a proper `ContactForm` representation. So, we will add more fields to the `ContactForm` proto message and make sure our service handles them properly. Meaning, we will need to expand the representation of a `ContactForm` and also make sure all information is properly persisted to MySQL DB.

## In this topic you will: 
* [Expand the `ContactForm` entity](#contactform-entity)
* [Implement simple counting by exposing a new API](#simple-counting)
* [Get the code to production](#get-production)

## Expand the `ContactForm` entity  <a name="contactform-entity"></a>

1. [Update the proto file](#update-proto)
1. [Modify the domain objects](#domain-objects)
1. [Update the AutoMapper](#update-the-automapper)
1. [Fix the tests](#fix-the-tests)

### 1. Update the proto file <a name="update-proto"></a>
The `ContactForm` proto message is defined in the `contact_us.proto` file. Use this [proto guideline](https://bo.wix.com/wix-docs/rnd/platformization-guidelines#protobuf) for this task.

Let's assume we want to add the following to the `ContactForm` proto message:
* `phone`
* `email`
* `site_counters` (a counter for the number of times the `ContactForm` was clicked in a specific site). Notice that this should be a list of `SiteCounter` proto messages.

Make sure you use the appropriate Wix data types.

Let's also add some proto validations:
* `id` should be a Wix GuId representing contactFormId
* `name` should have a max Length of 150
* `description` should have a max length of 500
* `site_counter` should be Read Only (that is, it cannot be updated by a request)

After you edit the `contact_us.proto` file, build your project using Bazel (either from CLI, Intellij Bazel icon or hitting <kbd>CMD</kbd>+<kbd>F9</kbd>.<br>  
Verify that the code was generated with the fields you added. To do that - examine the `ContactForm.class` that was generated based on your `ContactForm` proto message.



### 2. Modify the domain objects <a name="domain-objects"></a>
You've modified the proto API objects, but didn't actually change the implementation.
Now, we will modify the implementation so we can actually save the data that was added.

**What are Domain Objects?**  

We use [scalapb](https://scalapb.github.io/) to generates class cases and stub classes based on the proto file, for example the `Contact`proto message that we have defined in `contact_us.proto` generated a `ContactForm.class`. 
As a best practice, we convert these API objects to domain objects before we pass them to our core business logic. This is to prevent leakage between the API and domain layers that have different objects with different responsibilities (one is exposed as API and the other is used internally by your service).

**Let's change some code:**

Find the domain object and add the missing fields (with respect to the change of the `ContactForm` proto message). But where is this domain object case class? Try to find it yourself. A good starting point is the `ContactUsImpl` class that actually implements you API.<br>
When adding the missing fields to your domain object:
* Use Scala's `Option` for optional fields.



### 3. Update the AutoMapper<a name="update-the-automapper"></a>
The `Mapper` object was created for you, it's a utility that uses [AutoMapper](https://github.com/wix-private/server-infra/tree/master/aglianico/automapper) for converting api objects to domain objects and vice versa.

Based on the [AutoMapper](https://github.com/wix-private/server-infra/tree/master/aglianico/automapper) readme, try to change the `Mapper#toDomain(ContactForm, String, Option[ContactFormId])` function, to disregard the `ContactForm.siteCounters` field.



### 4. Fix the tests <a name="fix-the-tests"></a>
If you compile now you will see some tests still don't pass (specifically `ContactUsDaoIT`). This is because the created a `ContactFormEntity` is missing a few new fields. Try to fix the compilation errors and make sure all tests pass.
____________
> **NOTE**: Before running the tests make sure Docker Desktop is running! If it is not, then all tests will fail.<br/> 
> This is because your tests start a MySQL Docker container and your service expects a DB up and running. <br/> 
> If you do not have Docker Desktop, then install it. (<a href="https://docs.docker.com/docker-for-mac/install/">Install Docker Desktop for Macs</a>).
_____________
You can also update the ITs. 
* See the `ContactUsIT#create#create contactForm` test. It creates a contactForm and make sure it's properly saved. To make sure your added properties are properly saved, you need to update the `ContactFormRandoms#randomContactForm` function (which the test uses) to also populate the newly added properties. 
>  Notice that the default value for the  `siteCounters` argument (in `ContactFormRandoms#randomContactForm`) could be `Nil`. Why? Because it's  marked as `read-only` in your proto API and should not be sent by the client when calling your service.



____________
> **NOTE**: This is a good time to commit + merge + deploy your changes.
_____________

## Implement simple counting by adding a new endpoint <a name="simple-counting"></a>
Until now you've only added properties to the `ContactForm`. 

Now we want to add a new API endpoint to the service API with new functionality.<br>
Since the _Contact Us Service_ is to be used by sites to hold and manage contact forms, we must keep track on the number of times a specific `ContactForm` is contacted. 
To do this, you need to expose a functionality to increment a contact form counter by 1.

1. [Add API to a proto file](#add-api)
1. [Run a test](#run-a-test)
1. [Implement the incrementCounter endpoint](#implement-endpoint)

### 1. Add API to a proto file <a name="add-api"></a>
The first thing to do in order to expose a new API is to define it. 
* We want to define a new proto message and a proto rpc method. 
* The message should hold both the `contact_form_id` and the `meta_site_id`, to enable your service to know which counter to increment. 
* Expose the endpoint via a POST REST call. (This could be done by adding another annotation on your proto defined rpc method.)

1. Follow the [proto guidenline doc](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/protobuf#platformization-guidelines_protobuf_services) and add an API to your service.



1. After you add the API to the proto, compile the code. To do this, you need to implement the new method to enable compilation to pass. 
Since we want to write the code in TDD (test-driven development), we will use Scala's placeholder [`???`](https://stackoverflow.com/questions/31302524/what-does-the-triple-question-mark-mean-in-scala).  

### 2. Run a test <a name="run-a-test"></a>
Now that you have the `IncrementCounter` API and your code compiles, you can start implementing the new functionality.   
Since we are practicing TDD (Test Driven Development), we will write the tests before we actually implement the method.  

1. Let's stop here and discuss [Testing at Wix](../explanations/testing-at-wix.md).

1. Welcome back! Now you're ready to write your tests. Stop for a few minutes, and try to think what are the tests that you want to write for this endpoint. How do you expect it to behave? What are its expected side effects?

1. Did you do some thinking? Great! The test spec that you have thought of should have the following structure in the `ContactUsIT` class. Create the test spec. 
    
    ```scala
    class ContactUsIT ... {
    ...
    
        "incrementCounter" should {
            "increment the contact forms's counter by 1" in new BaseContext {
                // Your test here
            }
        }
    }
    ```

1. Implement your test. When finished, look at the solution below.


    
1. Run the test - it fails. 
   If you look at the test log (outputted to your console) you'll find a `NotImplementedError` exception. This is because you did not yet implement the `ContactUsImpl#incrementCounter` method. You'll do that next.

### 3. Implement the incrementCounter endpoint <a name="implement-endpoint"></a>
It's now time to write the code that actually increments the counter upon a call to your service's `incrementCounter` endpoint.
* Change the `ContactUsImpl#incrementCounter` from `???` to a proper implementation so that the test will pass.
* If you're new to Scala, it might be a good time to read about [for comprehension and Future](https://stackoverflow.com/questions/19045936/scalas-for-comprehension-with-futures)




## Get the code to production <a name="get-production"></a>
Now we would like to test our new API in production
1. Push your code, create a PR and merge it.
2. GA in Lifecycle.
3. Call the new API via [fire-console](https://pbo.wix.com/fire-console/) and make sure the counter was updated (using the `CreateContactForm`, `IncrementCounter` and `GetContactForm` endpoints, or just via your favourite DB workbench).
> :tipping_hand_woman: Psst **Did you remember** to generate an **authorization aspect** in Fire Console? Please do so to avoid getting a failed response. See an error message example `FailedPrecondition (9): App [4b74bdd1-2b0b-4c75-a82d-7a981c57be16] is not installed` error.


### Where to go next?
[Step 5 - Secure authorization and authentication](5-secure-authorization-and-authentication.md)
