SortOrder: 1
# About the API


The Domain Register API allow you to:

- register a domain.


## High level Diagram

![alt text](https://s3.amazonaws.com/wixplorer-readme-images/domain-registrations%2Fdomain-register-diagram.png)

## Terminology

### Domain

- **Wix Domain**
  <br>
  A domain purchased and managed by Wix. 


## Limitations


## Error Handling

The api will throw errors if something goes wrong.

User input validation for domain registration:

- domain - required field.
- domain - must be in a hostname domain format.
- product_instance_id - required.
- contacts - required field.
- contacts.registrant - required
- contacts.registrant.firstName - required
- contacts.registrant.lastName - required
- contacts.registrant.email - required
- contacts.registrant.address - required
- contacts.registrant.city - required
- contacts.registrant.postalCode - required
- contacts.registrant.countryCode - required
- contacts.registrant.phone - required

Business error thrown by the API:

- AccountNotFound - if no user found with the specified account_id
- SiteNotFound - if no meta site found with the specified site_id
