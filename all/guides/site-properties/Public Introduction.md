SortOrder: 1
# About Site Properties

Site Properties are a set of business-related values associated with a particular Wix site. It is modelled as a stream of versioned events (as in an event-sourced system), which can be accessed as-is or materialized into snapshots; a snapshot is essentially a key-value container that represents site properties at a given point in time (or version).   

The Site Properties API is a service that holds all the public information about the site/business in one single place, including its name, address, contact info and more. 
It’s a single source of truth for this data across Wix.  

Site owners enter this information in the Wix Business Manager under Settings > General Info.

## Site Properties Info
- **Basic Info**: Business Name, Site Display Name, Logo, Description, Categories  
- **Contact Info**: Email, Phone, Fax  
- **Location**: Address (Country, State, City, Street, Apartment, Zip Code, Description, Has physical address)  
- **Region**: Locale, Language, Multilingual, Payment Currency, Timezone  
- **Opening Hours**: Business Schedule   

### Language vs. Locale
- Language (e.g. “en”) determines the site language that will be displayed to the user of user on the site. It’s a list of (currently) 29 languages that Wix supports.  
It also used in the html of the site for SEO and browser support purposes.  
- Locale (e,g, “en-US”) determines the formats that will be used across the site: date and time, currency, units and measurements, and first day of the week.    

Wix saves and supports both, in order to support all locales, even though Wix doesn't support all languages, and to allow special combinations, such as a site in Japanese for users in the US.

### Site Categories Examples
Business  
Online Store  
Photography 
Music & Culture  
Design  
Restaurants & Food 
Accommodation   
Travel & Tourism  
Portfolio & CV  
Health & Wellness  
Fashion & Lifstyle  
Community & Education  
Consulting & Coaching   
Advertising & Marketing  
Automotive & Cars  
Real Estate  
Finance & Law  
Technology & Apps  
Pets & Animals  
Home & Electronics  
Travel & Documentary 
Weddings & Celebrations  
Conferences & Meetups  
Sport & Recreation  
Religion & Non Profit  
Creative Arts  
Performing Arts  
Promotional Page
Sports & Outdoors  
Kids & Babies 
Parenthood  
Art & Culture  
Leisure & Activities  
News & Opinions  
Business & Management  
Lifestyle  
