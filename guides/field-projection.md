# Field Projection

Some endpoints support field projection, which allows you to control which fields are returned in the response object.

**Fields** are predefined enumerations that may be either:
  - Named sets of fields provided by Wix for common use cases.
  - Individual field names.

In some cases, specific `fields` values may be protected by additional permissions.

## Legacy field projection

Legacy APIs offer `fieldsets` and `fields` to manage returned fields:

- **Fieldsets** are predefined and named sets of fields. Fieldsets are provided by Wix for common use cases.
For example, in the [Contacts API](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/contacts/contact-v4/contact-object), the `FULL` fieldset returns the full contact object,
and the `BASIC` fieldset returns the contact's name, primary email, and primary phone number.

  The default fieldset is typically the full object, although some APIs may specify a different default fieldset.  
  See each API's documentation for specific details.

- **Fields**, on the other hand, allow you to supply a list of field names to return.

If you specify fieldsets and projected fields together in a request,
the union of all included fields is returned.
For example, if you specify the `BASIC` fieldset and the `info.birthdate` field,
all fields included in the `BASIC` fieldset and `info.birthdate` are returned.

If neither fieldsets nor projected fields are specified, the default fieldset is returned.
