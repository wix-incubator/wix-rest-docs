# About the API


The Domain Search API allow you to:

- check a domain availability.
- suggest domains.


## High level Diagram

![alt text](./assets/domain-search.png)

## Terminology

### Domain

- **Availability**
  <br>
- A domain that has already been taken has availability equal to false.
- A domain that is still available for purchase has availability equal to true.

- **Suggestion**
  <br>
- A domain that is available for purchase at Wix.


## Error Handling

The api will throw errors if something goes wrong.

User input validation for the check availability API:

- domain - required field.
- domain - must be in a hostname domain format.

User input validation of the suggest API:

- query - required field, can be any alphanumeric text with spaces and hyphens
- tlds - a list of tlds, i.e. ["com", "net", "org"]
- limit - optional number, can be between 1 and 20

Business error thrown by the API:
