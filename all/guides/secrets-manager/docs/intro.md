SortOrder: 0
# Secrets Manager

## Goal
Providing a safe and secure way of storing sensitive values that are used by Corvid site (in user-code). This comes as an alternative to hard-coding such values in backend-code, which was the safest way to limit access to those keys to the site's code and site-owner only.

## Concepts

### Secret
A secret is composed of the following fields:
1. `name` - mandatory. Used to retreive the secret value.
1. `value` - mandatory. The sensitive value we'd like to use in user-code
1. `description` - optional. Some human-friendly description of the secret (e.g., "github token")
1. `id` - read-only. The id assigned to the secret value by the Secrets-Manager, and does not change (contrary to the name, which might be updated by the user). Used for all API opertaions, expect for getting a secret by name.
1. `created_at`, `updated_at` - timestamps of creation and last-update of the secret (partial or full)

### Using a secret value
Expect for managing the keys in the Business-Manager "Secerts Manager" section, the secret value can be cosumed by Corvid backend-code, using the [Secrets EDM](https://github.com/wix-private/elementory-dynamic-modules/tree/master/wix-secrets-backend).
