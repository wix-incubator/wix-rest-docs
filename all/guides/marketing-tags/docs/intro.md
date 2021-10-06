SortOrder: 0
# About Marketing Tags

With Wix Marketing Tags, site owners can embed marketing tags in their website. The supported marketing tags are:

* [**Google Ads Conversion tag**](https://support.google.com/tagmanager/answer/6105160?hl=en&ref_topic=6334091)

    > **Note:** The **Google Ads Conversion tag** was previously called **Google AdWords tag**.
* [**Google Analytics tag**](https://support.google.com/tagmanager/topic/6333310?hl=en&ref_topic=3002579)


    > **Note:** Both [**Google Universal Analytics tags**](https://support.google.com/tagmanager/answer/6107124?hl=en&ref_topic=6333310) and [**Google Analytics 4 tags**](https://support.google.com/tagmanager/answer/9442095?hl=en&ref_topic=6333310) are supported.
* [**Yandex Metrica tag**](https://yandex.com/support/metrica/index.html)
* [**Facebook Pixel tag**](https://developers.facebook.com/docs/facebook-pixel/)
* [**Google tag**](https://support.google.com/tagmanager/answer/6102821?hl=en&ref_topic=3441530)


These marketing tags enable site owners to track user activity, ad conversion rates, and more.

> **Note:** Only one marketing tag of each type is supported per Wix site.


The Marketing Tags APIs allow your app to:

* List marketing tags
* Create and update marketing tags
* Delete marketing tags


## Terminology

* **Domain:** Specifies which website is associated with the marketing tag.

    > **Note:** When the site owner changes the domain of a Wix site, the embedded marketing tags won’t load anymore. To update the domain use the [Upsert Marketing Tags](https://dev.wix.com/api/rest/marketing/marketing-tags/upsert-marketing-tags) endpoint. Currently, there is no way to sign up for notifications when a site owner changes their domain name.
* **Tracking ID:** Specifies which external ID is associated with the site owner. Learn more about each tracking ID in the corresponding object description. These are the supported external IDs:

    | Marketing Tag | External ID Name | ID Format| 
    |-|-|-|
    | Google Ads Conversion tag | Conversion ID | AW-123456789 |
    | Google Universal Analytics tag | Analytics ID | UA-12345-1 |
    | Google Analytics 4 tag | Measurement ID | G-12345  |
    | Yandex Metrica tag | Tag number | 123456789 |
    | Facebook Pixel tag | Pixel ID  | 123456789  |
    | Google tag | Tag Manager Container ID | GTM-12345 |
