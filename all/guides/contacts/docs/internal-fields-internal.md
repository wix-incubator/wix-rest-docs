SortOrder: 10
# Internal Fields

Some fields are for Wix internal use
and don't appear in the other public facing documents.
We will list them in this article.

## Internal Contact Field Mask Fields

> **Note:**
> You may see a deprecation note for field masks.
> The note applies only to external TPAs.
> We'll continue to support field masks for internal use.

| Field                                |
|--------------------------------------|
| `info.assignedUserIds`               |
| `info.extendedFields.members.mobile` |

## Internal Contact Projection Fields

| Field                  |
| ---------------------- |
| `info.assignedUserIds` |

## Internal Filters and sort

| Field                                  | Description                                    | Query Filter Operators | Possible Values         | Sorting |
|----------------------------------------|------------------------------------------------| ---------------------- |-------------------------|---------|
| info.assignedUserIds                   | Site contributors assigned to the Contact      | $hasSome, $hasAll      | String                  |         |
| info.extendedFields.members.mobile     | Is Contact a member mobile                     | $eq,$ne                | Boolean: `true`/`false` |         |

## Future Filters and sort (alpha)


| Field                               | Supported Filters                             | Sortable | Searchable |
|-------------------------------------|-----------------------------------------------|----------|------------|
| `primaryEmail.email`                | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable |            |
| `primaryEmail.subscriptionStatus`   | `$eq`, `$ne`,`$in`, `$nin`                    |          |            |
| `primaryEmail.deliverabilityStatus` | `$eq`, `$ne`,`$in`, `$nin`                    |          |            |
| `primaryPhone.phone`                | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |            |
| `primaryPhone.e164Phone`            | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |            |
| `primaryPhone.formattedPhone`       | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable |            |
| `primaryPhone.countryCode`          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable |            |
| `primaryPhone.subscriptionStatus`   | `$eq`, `$ne`, `$in`, `$nin`                   |          |            |
| `lastActivity.date`                 | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |            |
