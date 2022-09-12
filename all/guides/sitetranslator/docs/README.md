SortOrder: 0
# Site Translator 

This service is used to translate an entire site with one request.</br>

This service contain two main endpoints:
* GetSiteTranslatablesProperties - get site translation status
* TranslateSite - translate entire site

The suggested way to use this service it to first run GetSiteTranslatablesProperties to make sure you have enough word credit to translate the remaining untranslated content of the site. If the credit is sufficent then run TranslateSite to translate the remaining content.


### Expand content coverage

Site translator is working using an SPI to read and update translation content.</br>
For more info read [TranslationContentProvider SPI](https://github.com/wix-private/linguist/blob/master/site-translator/spi-proto/docs/README.md)
