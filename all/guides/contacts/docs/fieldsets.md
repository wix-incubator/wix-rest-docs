SortOrder: 4
# Fieldsets and Projected Fields

Some endpoints allow you to return a partial `contact` object
with only the fields you request.
To do this, you can use fieldsets and projected fields.
For common use cases, we provide fieldsets,
which are predefined named sets of fields.
If you don’t see a fieldset for your use case,
you can use projected fields, where you specify fields to return.

Fieldsets and field projection are available for these endpoints:

- [Get Contact][get-contact]
- [List Contacts][list-contacts]
- [Query Contacts][query-contacts]

> **Note:**
> If you use a combination of fieldsets and projected fields,
> or if you use multiple fieldsets,
> `contact` will be returned with all of the requested fields.

## Valid Contact Projection Fields

You can use a field projection to return a partial `contact` object
with only what you request in the `fields` array.

The following fields can be returned in a partial object
by specifying them in `fields`:

> **Note:**
> `id` and `revision` are always returned,
> even if you don’t include them in the `fields` array in your request.

- `id` (always returned)
- `revision` (always returned)
- `source`
- `createdDate`
- `updatedDate`
- `lastActivity`
- `picture`
- `primaryInfo`
- `info.name`
- `info.emails`
- `info.phones`
- `info.addresses`
- `info.company`
- `info.jobTitle`
- `info.birthdate`
- `info.locale`
- `info.labelKeys`
- `info.extendedFields`

## Contact Fieldsets

Fieldsets let you return a predefined partial `contact` object.
Fieldsets are built by Wix for common use cases.
You’ll specify fieldsets in the `fieldsets` array in your request.

The following table shows the fields that are returned with each fieldset.
If `fieldsets` is empty or missing, the `BASIC` fieldset is returned:

| Fieldset | Returned Fields |
|---|---|
| `BASIC` (default) | `id`, `revision`, `info.name.first`, `info.name.last`, `primaryInfo.email`, `primaryInfo.phone` |
| `COMMUNICATION_DETAILS` | `id`, `revision`, `info.name.first`, `info.name.last`, `info.emails`, `info.phones`, `info.addresses` |
| `EXTENDED` | `id`, `revision`, `info.name.first`, `info.name.last`, `primaryInfo.email`, `primaryInfo.phone`, `info.extendedFields` |
| `FULL` | All fields |

[get-contact]: crm.contacts.contacts-v4.get-contact
[list-contacts]: crm.contacts.contacts-v4.list-contacts
[query-contacts]: crm.contacts.contacts-v4.query-contacts
