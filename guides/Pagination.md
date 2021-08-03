
<details><summary>Show Solution</summary>

```proto
message ContactForm {
    google.protobuf.StringValue id = 1 [(wix.api.format) = GUID, (wix.api.readOnly) = true];    // ContactForm's unique ID
    google.protobuf.StringValue name = 2 [(wix.api.maxLength) = 150];                           // ContactForm's name
    google.protobuf.StringValue description = 3 [(wix.api.maxLength) = 500];                    // ContactForm description
    google.protobuf.StringValue phone = 4 [(wix.api.format) = PHONE];
    google.protobuf.StringValue email = 5 [(wix.api.format) = EMAIL];
    repeated SiteCounter site_counters = 6 [(wix.api.readOnly) = true];
}

message SiteCounter {
    string meta_site_id = 1 [(wix.api.format) = GUID];
    int32 counter = 2 [(wix.api.readOnly) = true];
}
```

</details>

<details><summary>Show Solution</summary>
Update <code>ContactFormEntity</code> case class in <code>dao.scala</code>

```scala
case class SiteCounterEntity(metaSiteId: String, counter: Int)
case class ContactFormEntity(id: ContactFormEntityId,
                         @searchable name: String,
                         description: Option[String],
                         phone: Option[String],
                         email: Option[String],
                         siteCounters: Seq[SiteCounterEntity],
                         version: Option[Long] = None) extends Entity[ContactFormEntityId]                         
```
</details>


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
Because we've added <code>phone</code>, <code>email</code> and <code>siteCounters</code> fields (to both proto and domain objects) we need to map between them respectively.
<ul>
<li><code>phone</code> and <code>email</code> fields have the same type of proto and entity counterparts (<code>String</code>). Therefore, we do not need to explicitly add them to the mapping. They will be auto mapped for us, this is <a href="https://github.com/wix-private/server-infra/tree/master/aglianico/automapper#basic-usage"> Auto Mapper</a>'s guarantee.
<li><code>SiteCounter</code> field will be correctly mapped too, as AutoMapper automatically derives transformations for simple case classes.
    <ul>
<li>For mapping between a proto to an entity, notice that we've stated <code>.withFieldConst(_.siteCounters, Nil)</code>, this is because the proto states that <code>siteCounters</code> is a read-only property. Therefore, the server should disregard requests from client that try to update this property.</li></ul>
</li></ul>

</details>

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

<details><summary>Show Solution</summary>

```proto
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
</details>

    
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

<details><summary>Show Solution</summary>
    
```scala
class ContactUsImpl ... {
    ...
    override def incrementCounter(request: IncrementCounterRequest)(implicit callScope: CallScope): Future[IncrementCounterResponse] = {
        val context = contextResolver.getContext
        for {
            contactForm <- contactUsDao.findByIdOrFail(ContactFormEntityId(ContactFormId.guidOf(request.contactFormId), TenantId.guidOf(context.instanceId)))
            updatedContactForm = contactForm.copy(siteCounters = incrementCounterForSite(contactForm.siteCounters, request.metaSiteId))
            _ <- contactUsDao.update(updatedContactForm)
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
