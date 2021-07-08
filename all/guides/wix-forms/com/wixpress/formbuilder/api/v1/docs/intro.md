SortOrder: 0
# Wix Forms

## What is it?

Wix Forms enables our users to create and add any type of form to a Wix Site. 

## What can users do with it?

Wix users can find a variety of templates, such as Contact Form and Job Application Form,
and customize the design of these forms as well as change the fields that are included in
the form in order to collect the information that they need from their site visitors.
Additionally, users can choose to sync the form fields to the contact that is created once
the site visitor submits the form, enabling the user to automatically link the information
they collect from the form to the relevant contact.

When site visitors submit a form the user will be able to see it in:
 
 * Wix Inbox
 * The email account the user sets in their form settings
 * The submission table in the site dashboard 

## Main entities

### FormDetails

The `FormDetails` entity represents a custom form. A form has a lifecycle with the following stages:

 * `DRAFT` - Form was created in the editor, but was not yet published
 * `PUBLISHED` - Form is published and available on the site
 * `DELETED` - Form was published but removed from the site
 * `DISCARDED` - Form was created in the editor, but deleted before the site was published
