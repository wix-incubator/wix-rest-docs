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

<details><summary>Show Solution</summary>

<pre><code>
message ContactForm {
    google.protobuf.StringValue id = 1 [(wix.api.format) = GUID, (wix.api.readOnly) = true];    // ContactForm's unique ID
    google.protobuf.StringValue name = 2 [(wix.api.maxLength) = 150];                           // ContactForm's name
    google.protobuf.StringValue description = 3 [(wix.api.maxLength) = 500];                    // ContactForm description
    google.protobuf.StringValue phone = 4 [(wix.api.format) = PHONE];
    google.protobuf.StringValue email = 5 [(wix.api.format) = EMAIL];
    repeated SiteCounter site_counters = 6 [(wix.api.readOnly) = true];
}<br>

message SiteCounter {
    string meta_site_id = 1 [(wix.api.format) = GUID];
    int32 counter = 2 [(wix.api.readOnly) = true];
}
</code></pre></details>


### 2. Modify the domain objects <a name="domain-objects"></a>
You've modified the proto API objects, but didn't actually change the implementation.
	@@ -75,8 +79,8 @@ When adding the missing fields to your domain object:

<details><summary>Show Solution</summary>
Update <code>ContactFormEntity</code> case class in <code>dao.scala</code>

```scala
case class SiteCounterEntity(metaSiteId: String, counter: Int)
case class ContactFormEntity(id: ContactFormEntityId,
                         @searchable name: String,
	@@ -85,22 +89,24 @@ case class ContactFormEntity(id: ContactFormEntityId,
                         email: Option[String],
                         siteCounters: Seq[SiteCounterEntity],
                         version: Option[Long] = None) extends Entity[ContactFormEntityId]
```
</details>

### 3. Update the AutoMapper<a name="update-the-automapper"></a>
The `Mapper` object was created for you, it's a utility that uses our [Chimney](https://scalalandio.github.io/chimney/) wrapper called [AutoMapper](https://github.com/wix-private/server-infra/tree/master/iptf/automapper) for converting api objects to domain objects and vice versa.

Based on the [AutoMapper](https://github.com/wix-private/server-infra/tree/master/iptf/automapper) readme, try to change the `Mapper#toDomain(ContactForm, String, Option[ContactFormId])` function, to disregard the `ContactForm.siteCounters` field.

<details><summary>Show Solution</summary>

```scala
def toDomain(in: ContactForm, tenantId: String, forCreate: Option[ContactFormId] = None): ContactFormEntity =
  in.mappingFor[ContactFormEntity]
    .withFieldComputed(_.id, s => ContactFormEntityId(forCreate.getOrElse(ContactFormId.guidOf(s.id.get)), TenantId.guidOf(tenantId)))
    .withFieldConst(_.version, None)
    .withFieldConst(_.siteCounters, Nil)
    .transform
```

<h4>Let's explain what we just did here</h4>
We wanted the <code>Mapper</code> to properly convert all fields from proto to domain object and vice versa.<br>
	@@ -111,6 +117,7 @@ Because we've added <code>phone</code>, <code>email</code> and <code>siteCounter
    <ul>
<li>For mapping between a proto to an entity, notice that we've stated <code>.withFieldConst(_.siteCounters, Nil)</code>, this is because the proto states that <code>siteCounters</code> is a read-only property. Therefore, the server should disregard requests from client that try to update this property.</li></ul>
</li></ul>

</details>

### 4. Fix the tests <a name="fix-the-tests"></a>
	@@ -125,28 +132,30 @@ You can also update the ITs.
>  Notice that the default value for the  `siteCounters` argument (in `ContactFormRandoms#randomContactForm`) could be `Nil`. Why? Because it's  marked as `read-only` in your proto API and should not be sent by the client when calling your service.
<details><summary>Show Solution</summary>

```scala
trait ContactFormRandoms extends RandomTestUtils {
    ...
    ...
    ...
    def randomContactForm(id: Option[String] = None,
                    name: Option[String] = randomStrOpt,
                    description: Option[String] = Some(randomStr),
                    phone: Option[String] = Some(s"${randomNumberWith(3)}-${randomNumberWith(7)}"),
                    email: Option[String] = Some(randomEmail),
                    siteCounters: Seq[SiteCounter] = Nil): ContactForm = {
        ContactForm(
          id = id,
          name = name,
          description = description,
          phone = phone,
          email = email
        )
    }
}
```
</details>

____________
> **NOTE**: This is a good time to commit + merge + deploy your changes.
	@@ -172,19 +181,22 @@ The first thing to do in order to expose a new API is to define it.
1. Follow the [proto guidenline doc](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/protobuf#platformization-guidelines_protobuf_services) and add an API to your service.

    <details><summary>Show Solution</summary>

    <pre><code>
    rpc IncrementCounter (IncrementCounterRequest) returns (IncrementCounterResponse) {
        option (google.api.http).post = "/v1/contactForm/{contact_form_id}/increment";
        option (.wix.api.maturity) = ALPHA;
        option (.wix.api.required) = "IncrementCounterRequest.contact_form_id";
        option (.wix.api.required) = "IncrementCounterRequest.meta_site_id";
    }

    message IncrementCounterRequest {
        string contact_form_id = 1 [(.wix.api.format) = GUID];
        string meta_site_id = 2 [(.wix.api.format) = GUID];
    }
    message IncrementCounterResponse {}
    ```
    </code></pre></details>

1. After you add the API to the proto, compile the code. To do this, you need to implement the new method to enable compilation to pass.
Since we want to write the code in TDD (test-driven development), we will use Scala's placeholder [`???`](https://stackoverflow.com/questions/31302524/what-does-the-triple-question-mark-mean-in-scala).
	@@ -212,18 +224,24 @@ Since we are practicing TDD (Test Driven Development), we will write the tests b
    ```

1. Implement your test. When finished, look at the solution below.

    <details><summary>Show Solution</summary>

    ```scala
    "incrementCounter" should {
      "increment the contact form's counter by 1" in new BaseContext {
      val siteId = UUID.randomUUID().toString
      val contactForm = givenContactForm(randomContactForm())

      contactUs.incrementCounter(IncrementCounterRequest(contactForm.id.get, siteId)).shortAwait

      contactUs.getContactForm(GetContactFormRequest(contactForm.id.get)).map(_.contactForm) must
        beSome(contactForm.copy(siteCounters = Seq(SiteCounter(siteId, 1)))).await.eventually
      }
    }

    ```
    </details>

1. Run the test - it fails.
   If you look at the test log (outputted to your console) you'll find a `NotImplementedError` exception. This is because you did not yet implement the `ContactUsImpl#incrementCounter` method. You'll do that next.
	@@ -232,27 +250,32 @@ Since we are practicing TDD (Test Driven Development), we will write the tests b
It's now time to write the code that actually increments the counter upon a call to your service's `incrementCounter` endpoint.
* Change the `ContactUsImpl#incrementCounter` from `???` to a proper implementation so that the test will pass.
* If you're new to Scala, it might be a good time to read about [for comprehension and Future](https://stackoverflow.com/questions/19045936/scalas-for-comprehension-with-futures)

<details><summary>Show Solution</summary>

```scala
class ContactUsImpl ... {
    ...
    override def incrementCounter(request: IncrementCounterRequest)(implicit callScope: CallScope): Future[IncrementCounterResponse] = {
        val context = contextResolver.getContext
        for {
            contactForm &lt;- contactUsDao.findByIdOrFail(ContactFormEntityId(ContactFormId.guidOf(request.contactFormId), TenantId.guidOf(context.instanceId)))
            updatedContactForm = contactForm.copy(siteCounters = incrementCounterForSite(contactForm.siteCounters, request.metaSiteId))
            _ &lt;- contactUsDao.update(updatedContactForm)
        } yield IncrementCounterResponse()
     }
     private def incrementCounterForSite(siteCounters: Seq[SiteCounterEntity], metaSiteId: String): Seq[SiteCounterEntity] = {
        val (beforeMsId, afterMsId) = siteCounters.span(_.metaSiteId != metaSiteId)
        (beforeMsId :+
            afterMsId.headOption.map(c => c.copy(counter = c.counter + 1))
                .getOrElse(SiteCounterEntity(metaSiteId, 1))) ++
            afterMsId.drop(1)
  }
}
```
</details>


## Get the code to production <a name="get-production"></a>
Now we would like to test our new API in production
