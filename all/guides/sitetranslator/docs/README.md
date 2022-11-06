SortOrder: 0
# About SiteTranslator 

This API can be used to:

**Purpose #1.** Translate with machine translation, in one request, all site content that hasn't been translated yet.

**Purpose #2.** Get the translation status of any site.

To translate site content with machine translation, the site needs to have a sufficient amount of words credit (each site has a default amount of words credit and the user can get more credit by purchasing a translation package). Therefore, the suggested way to use this API is first to run GetSiteTranslatablesProperties to make sure there are enough word credits to translate the remaining content of the site. If there are enough word credits, then run TranslateSite.

### Expand content coverage

SiteTranslator uses an SPI to read and update translation content. [Read more about the TranslationContentProvider SPI](https://github.com/wix-private/linguist/blob/master/site-translator/spi-proto/docs/README.md).
