# Field Projection

Some endpoints support field projection, which allows you to control which fields are returned in the response object. This is done with the use of fieldsets and projected fields.

**Fieldsets** are predefined, named sets of fields. Fieldsets are provided by Wix for common use cases. For example, in the Contacts API, the `FULL` fieldset returns the full contact object, and the `BASIC` fieldset returns the contact's name, primary email, and primary phone number.

The default fieldset is typically the full object, although your API may specify a different default fieldset. See your API's documentation for specific details.

**Projected fields**, on the other hand, allow you to supply a list of fields to return.

If you specify fieldsets and projected fields together in a request, the union of all included fields is returned. For example, if you specify the `BASIC` fieldset and the `info.birthdate` field, all fields included in the `BASIC` fieldset and `info.birthdate` are returned.

If neither fieldsets nor projected fields are specified, the default fieldset is returned.
