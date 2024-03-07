SortOrder: 2
# About the Registration Form API

Site owners can customize a registration form for the site visitor to fill out with their contact details, and other information, as relevant. 
Default fields are: first name, last name and email.
Custom form fields are supported, including free text fields, drop-down lists, and radio buttons, checkboxes, dates, addresses, and phones.

The registration form is made up of controls, each of which may include multiple field inputs (e.g., an address control including inputs for street address, city, state, country and zip code).

Each event has one published form and one draft (by default, each include first name, last name and email). 
All calls to add, update or delete controls affect the draft form, which can be published at any time with the Publish Draft endpoint.
