SortOrder: 0
# Introduction

The Moderation Rule Service empowers users to create custom moderation rules tailored to their specific requirements.
This API is particularly valuable for users seeking to maintain a safe and respectful comments section or combat spam on
their websites. Moreover, third-party app developers can integrate this API to moderate content within their own
products, whether it be another commenting application, a reviews collection system, or any other user-generated content
platform.

The Moderation Rule Service allows you to:

* Decide whose comments are being moderated
* Exclude specific user groups from moderation
* Select triggers that define what kind of content should be moderated
* Select if checked content should be sent for manual review or be rejected altogether

# Terminology

- **Rule**: is a predefined set of conditions and actions that govern user-created content on a website. It consists of
  three key components: the target audience (the intended recipients of the rule), triggers (events or conditions that
  activate the rule), and actions (the specific outcomes or behaviors that occur when the rule is activated).
- **Namespace**: A namespace is an organizational entity that allows different sets of rules to be assigned to content
  from specific sources within a website. This enables each consumer or component to have its own distinct set of rules,
  even if they are part of the same site. For instance, consider a website with a Wix Blog that includes integrated
  comments, as well as stores with integrated reviews. Since comments and reviews may require different moderation
  rules, namespaces like 'Comments/{BLOG_APP_ID}' or 'Reviews/{STORES_APP_ID}' can be defined to achieve this
  separation.
- **Member**: a user of user that is registered to the site
- **Visitor**: a site visitor that can leave comments as a guest, without logging in or registering to the site
- **Target audience**: subjects to whom the rule is applied. This could be site visitors, all members or newly
  registered members.
- **Trigger**: a specific condition or set of conditions that activate the rule. Triggers can be based on keywords,
  phrases, or submitted content. For example, a trigger could be a comment with links and media, or a comment with any
  given specific word, such as “bitcoin”.
- **Action**: The action that is performed when a rule is triggered. For example, action can be that comments are sent
  for manual moderation instead of getting published.
- **Exclusion**: Some members or a member group can be excluded from a given rule. If a member is excluded, it means
  that their comments are published automatically, without any manual approval.

# Limitations

* Client can only have up to 20 rules per namespace