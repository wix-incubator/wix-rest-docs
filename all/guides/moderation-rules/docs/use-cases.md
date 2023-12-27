SortOrder: 1
## Check if visitors comments contain links and media to prevent spam

In order to prevent the publication of spam content on your website, which often includes links to advertised
products or services, phishing sites, or fraudulent schemes, you decide to implement a custom moderation rule. You
observe that such comments are primarily submitted by visitors who comment without logging in. To address this issue,
you define the following components in your rule:

- **Target audience**: Visitors
- **Trigger**: Links
- **Action**: Reject

### Sample Flow

1. Client must create appropriate Rule using CreateRule API:

```json
{
  "rule": {
    "namespace": "comments",
    "name": "Moderate with links",
    "audience": {
      "type": "VISITORS"
    },
    "trigger": {
      "contentFeatures": {
        "videos": false,
        "images": false,
        "links": true
      }
    },
    "action": {
      "type": "NEEDS_MANUAL_APPROVAL"
    }
  }
}
```

2. Before publishing comment `Comment Service` must invoke `CheckContent` API to verify, that comment does not break any
   rules

```json
{
  "namespace": "comments",
  "content": {
    "plainText": "Visit my site! www.wix.com",
    "attributes": {}
  }
}
```

`CheckContent` API might respond with similar to:

```json
{
  "violations": [
    {
      "ruleId": "<rule-id>",
      "action": {
        "type": "NEEDS_MANUAL_APPROVAL"
      }
    }
  ]
}
```

3. Based on returned violations Comment Service must act accordingly

## Review all product reviews with one star rating

To mitigate the potential negative impact on your store's revenue caused by illegitimate or unhelpful product reviews,
you decide to implement moderation rules. Specifically, you want to review all reviews with a one-star rating that are
submitted by newly registered members. By doing so, you aim to ensure that only genuine and useful feedback is
published. To achieve this, you define the following components in your custom moderation rule:

- **Target audience**: Newly registered members
- **Trigger**: One-star rating
- **Action**: Send for manual approval

### Sample Flow

1. Client must create appropriate Rule using CreateRule API:

```json
{
  "rule": {
    "namespace": "reviews",
    "name": "No bad reviews",
    "audience": {
      "type": "VISITORS"
    },
    "trigger": {
      "attribute": {
         "name": "rating",
         "values": ["1"]
      }
    },
    "action": {
      "type": "NEEDS_MANUAL_APPROVAL"
    }
  }
}
```

2. Before publishing review `Reviews Service` must invoke `CheckContent` API to verify, that review does not break any
   rules

```json
{
  "namespace": "reviews",
  "content": {
    "plainText": "I don't like it!",
    "attributes": {
       "rating": "1"
    }
  }
}
```

`CheckContent` API might respond with similar to:

```json
{
  "violations": [
    {
      "ruleId": "<rule-id>",
      "action": {
        "type": "NEEDS_MANUAL_APPROVAL"
      }
    }
  ]
}
```

3. Based on returned violations Comment Service must act accordingly
