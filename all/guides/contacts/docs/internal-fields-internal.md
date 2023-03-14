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
| ------------------------------------ |
| `info.assignedUserIds`               |
| `info.extendedFields.members.mobile` |

## Internal Contact Projection Fields

| Field                  |
| ---------------------- |
| `info.assignedUserIds` |

## Internal Filters and sort

| Field                              | Description                               | Query Filter Operators | Possible Values         | Sorting |
| ---------------------------------- | ----------------------------------------- | ---------------------- | ----------------------- | ------- |
| info.assignedUserIds               | Site contributors assigned to the Contact | $hasSome, $hasAll      | String                  |         |
| info.extendedFields.members.mobile | Is Contact a member mobile                | $eq,$ne                | Boolean: `true`/`false` |         |
