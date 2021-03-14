SortOrder: 2
# Sample Use Case: Ads.txt

This article shares a possible use case for your app. You're certainly not limited to this use case, but it might be a helpful start to plan your app's implementation.

## Enable the owner of a blog to display advertisements on their site through a content discovery platform

The owners of a fitness blog would like to increase revenue by displaying advertisements on their Wix site. Your app will modify the existing Ads.txt file to enable a content discovery platform as an authorized seller.

### Append an existing Ads.txt file

To add an authorized digital seller, your app will call the **Append Ads.txt** endpoint. You’ll need to pass the platform’s name, account id, payment type, and tag id inside the `content` field of the `adsTxt` object. You can read more about the structure of Ads.txt files on the [IAB’s website][IABwebsite].


```sh
	curl -X PATCH https://www.wixapis.com/promote-seo-txt-file-server/v2/ads \
   	--header 'Content-Type: application/json;charset=UTF-8' \
   	--header 'Authorization: <AUTH>' \
   	--data-binary '{"adsTxt": {"content": "silveradexchange.com, pub-0000000000000001, RESELLER, b124y6716v287058"}}'
```

Notice that the content field in the response has two lines, separated by the new line (\n) control character.

```json
{
   "adsTxt": {
       "content": "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\nsilveradexchange.com, pub-0000000000000001, RESELLER, b124y6716v287058",
       "default": false,
       "subdomain": "www"
   }
}
```

[IABwebsite]: https://iabtechlab.com/ads-txt-about
