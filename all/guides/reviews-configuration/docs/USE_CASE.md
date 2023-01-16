SortOrder: 1
## Use Cases

This article shares some possible use cases your app can support. You are not limited to these use cases, but they can
be a helpful jumping off point as you plan your integration.

### Proactive moderation

Store owner may want to have moderation disabled by default, although if custom application detects abnormal
activity on site it could turn on reviews moderation by calling UpdateConfiguration API.

1. Define algorithm which detects abnormal activity in site.
2. Invoke QueryConfiguration to get existing review configurations which has moderation disabled:

    ```json
    {
      "filter": {
        "moderateContent": false
      }
    }
    ```

3. Invoke UpdateConfiguration API for each returned Configuration and set `moderateContent = true`:

    ```json
    {
      "configuration": {
        "id": "53c180b7-f2bf-4168-8bc8-d71c546a4130",
        "revision": 1,
        "moderateContent": true
      },
      "mask": {
        "paths": [
          "moderateContent"
        ]
      }
    }
    ```

