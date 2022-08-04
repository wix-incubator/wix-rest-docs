SortOrder: 1
# About Site Properties

Site Properties are a set of business-related values associated with a particular Wix site. They are modelled as a stream of versioned events (as in an event-sourced system), which can be accessed in their current state or materialized into snapshots. (A snapshot is essentially a key-value container that represents site properties at a given point in time, or in a given version).   

The Site Properties API is a service that holds all the public information about the site and business in a single place, including profile, contact details, schedule information, and consent policy. It’s a single source of truth for this data across Wix.  

Site owners enter this information in the Wix Business Manager under Settings > General Info.

## Site Properties Info
- **Profile**: Site Display Name, Business Name, Description, Logo
- **Contact**: Email, Phone, Fax, Address
- **Schedule**: Regular Business Hours, Special Exceptions
- **Region**: Locale, Language, Multilingual, Payment Currency, Timezone  
- **Consent Policy**: Default Consent Policy
- **Other Info**: Categories, Business Type

## Consent Policy
As per privacy regulation guidelines such as GDPR and CCPA, Wix has enabled a consent policy and adherence to the GDPR. Third parties can access and manage the default consent policy set for a site.
The consent policy includes the following types:
- **Functional**: used to remember choices users make to improve their experience (e.g. language).
- **Analytics**: lets the site/app owner understand how visitors use the website (e.g. which pages you visit), to provide statistics on how the website is used, improve the website by identifying any errors, and performance issues.
- **Advertising/Marketing**: used to collect information about the impact of marketing campaigns performed in other websites on users and non-users.
- **Essential**: lets the visitor move around the website and use essential features like secure and private areas.
- **Data To Third Parties**: lets the site/app owner share data with other parties (includes the sale of data, as well sharing data for essential or enhanced functionality, e.g., Google Analytics) - specifically for CCPA compliance.

> **Important**:  
> All apps are bound by the “Wix App Market – Partner Program Agreement”, which contains obligations related to privacy regulations (including honoring each site visitor’s decision about cookies).

For more information about the consent policy process for site owners, see the following:  
[Displaying a Cookie Banner On Your Site](https://support.wix.com/en/article/displaying-a-cookie-banner-on-your-site)  
[Adding a “Do Not Sell Data” Link to Your Wix Site](https://support.wix.com/en/article/adding-a-do-not-sell-data-link-to-your-wix-site)       
[Important Information About Editor Elements - Third Party Apps](https://support.wix.com/en/article/important-information-about-editor-elements-third-party-apps-custom-code-and-the-cookie-banner#third-party-apps)

### Language vs. Locale
- Language (e.g. “en”) determines the site language that will be displayed to the user of user on the site. It’s a list of (currently) 29 languages that Wix supports. It is also used in the html of the site for SEO and browser support purposes.  
- Locale (e,g, “en-US”) determines the formats that will be used across the site: date and time, currency, units and measurements, and first day of the week.    

Wix saves and supports both, in order to support all locales, even though Wix doesn't support all languages, and to allow special combinations, such as a site in Japanese for users in the US.

### Site Categories 
A category that the site owner selected when they set up their site.

**Examples:**   
Business  
Online Store  
Music  
Design  
Blog  
Beauty & Wellness  
Portfolio & CV  
Events  
Photography  
Restaurants & Food  
Fitness  
Technology Company  
Real Estate Agency  
Yoga Studio  
Financial Consultant  
Makeup Blog  
