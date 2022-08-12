SortOrder: 0
# Introduction

## Compliance Score Service API

The Compliance Score Service automatically determines the compliance level of a specific Wix Payments Account, based on multiple sources – enabling an Underwriting analyst to decide (automatically or manually) how to handle that Wix Payments Account.

The Compliance Score Service looks at a specific account, and turns to multiple sources, both internal and external, which cover multiple domains. After aggregating the sources’ outputs, the Compliance Score Service takes into account the outputs’ severity and the domains’ relative importance – and produces an overall score which reflects the account’s compliance level. In short, it collects data from multiple sources, and calculates a compliance level which is a basis for an automatic/manual decision.

With the Compliance Score Service, organizations with compliance-related liability can get a recommendation for end-users owning products / websites, the end-users’ transactions and the end-users themselves – so they would know how to act.

The Compliance Score Service enables your app to:

- Know the overall compliance level of an account
- Know the compliance status of a specific domain for an account
- Know what are the issues which caused this compliance level
- See the specific outputs of each source which analyzed the account

Please see details below under Use Cases.

## Terminology

- **Organization**: A party which provides products and/or services to its users, and may be liable for the users’ activity in terms of complying with government regulations and/or commercially-tied companies’ limitations.
- **User**: A party registered at an Organization. The user may be a legal entity, own a website, sell products/services and perform transactions.
- **Account**: An arrangement by which a user, her attributes, properties and activity are represented in the Organization’s system.
- **Ecosystem**: A group of systems, which is queried and returns with a response.
- **Score Engine**: A formula which takes the results of the responding Sub-Engines and returns a numerical score, representing the compliance level.
- **Sub-Engine**: Reflects rules for a specific domain using its corresponding Sources. Each Sub-Engine has its own Factors Table.
- **Source**: 3rd-party (or internal) service, that is queried and returns a list of results.
- **Domain**: A specified sphere of activity related for an Account’s activity, such as Website, Product, Person and Transaction
- **Factor**: A rule which generates a numeric score based on a single element of response from the specific Source. Its result goes through interpretation and scoring. Technically, it consists of a key and value. Key is matched to the corresponding rule from the Score Table, and value gets transformed to numeric score.
- **Factor Table**: A configurable list of Factors
- **Reason**: Reflecting the origin of a Factor result, in human language. Technically it’s a string from Factor Table, result of mapping a specific piece of response from Source to specific row in Factor Table

## Use Cases


![](https://s3.amazonaws.com/wixplorer-readme-images/compliancescoreservice%2Fcompliance_service_flow.png)
To be detailed

### 1. Know how to act with an Account based on its Compliance level

In this use case, an Organization wishes to know what to do with an Account that was recently created, or goes through a periodic/special investigation. The data is sent to the Compliance Score Service using the {methodName1} method. The Ecosystem responds with an overall compliance score, level and Reason (for example: 0, Low; or 75, High, Website category is Nutra AND products are categorized as Pharma). The Organization can now decide how to act (for example, automatically enable all the User’s possible activities; or instruct the User to remove Nutra-related elements and Pharma-related products from her website).

### 2. Check the Compliance of a specific Account Domain

In this use case, an Organization wishes to check a specific Domain of the User’s Account (for example, a Website). The data is sent to the Compliance Score Service using the {methodName2} method. The Ecosystem responds with a compliance score for that Domain along with the Reason (for example: 0; or 75, Website category is Nutra). The Organization can now decide how to act (for example, continue with having the User’s activities enabled; or instruct the User to remove Nutra-related elements from her website).

### 3. Check the Compliance of from a specific Source

In this use case, an Organization wishes to check a specific element of the User’s Account (for example, checking if a User appears in a Sanctions List). The data is sent to the Compliance Score Service using the {methodName3} method. The Ecosystem responds with the Domain’s updated compliance score, Reason and the Source’s raw data  (for example: 0, [Raw JSON}; or 100, User appears in SDN OFAC list, [Raw JSON]). The Organization can now decide how to act (for example, continue with having the User’s activities enabled; or conduct a thorough investigation on the User’s true identity).