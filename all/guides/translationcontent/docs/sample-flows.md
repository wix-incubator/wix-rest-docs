SortOrder: 1
# Sample Use Cases and Flows

> __⚠ This file is an example only ⚠__
>
> Replace the content with your own sample flows,
> following the prompts here.
>
> We put guidance in notes. Use the notes to fill in the blanks,
> then remove the notes (including this one).
>
> __Remember__:
>
> - You're writing for people who aren't on your team
>   and who aren't familiar with your API.
> - Include all the information you think is needed.
> - When your API is ready for final documentation,
>   a tech writer will help organize your thoughts,
>   fix the English,
>   and make sure the information is complete from an outsider's perspective.
>
>
> For tech writer guidance on writing sample flows, see
> [Sample Flow Article](https://wix-private.github.io/tw-cafe/style-guide/api-documentation-guidelines/intro-articles/sample-flow-article).
>
> Delete this note when you're done.

This article shares some possible use cases your app could support,
as well as a sample flow that could support each use case.
This can be a helpful jumping off point as you plan your app's implementation.

## Periodically export new Contents to an external ____

> ☝️ Each H2 introduces a flow.
> Start with a verb in the present tense.
> Don't use gerunds (verbs ending in -ing).
> For example, use "Create a new site" instead of "Creating a new site".
>
> Sometimes, a noun phrase is better than a verb.
> This is okay.
> For example, "Real-time 2-way sync with an external system"
> is less confusing than "Sync 2 ways with an external system in real time".
>
> Delete this note when you're done.

> 👇 **Introduce the flow**
>
> Write a sentence that leads into the flow, and end with a colon (`:`).
> If you're not sure what to write, try starting with "to"
> and paraphrasing the heading.
>
> Delete this note when you're done.

If a site owner _____,
you can export new Contents to an external _____.

To do this,
your app can _____:

> **Write the flow**
>
> To keep the flow scannable and readable,
> follow these guidelines:
>
> - **Use numbered steps**. <br />
>   Try to keep it to 10 steps or fewer.
>   (If you can't, don't worry.
>   A tech writer can help here.)
> - **Keep it linear**. <br />
>   Avoid "if this, then do that" options.
>   If your flow branches in multiple directions,
>   split it into multiple flows,
>   each with a different stated use case.
>
> The flow below is an example.
> Modify it to fit your use case.
>
> Delete this note when you're done.

1. For the first load after the app is installed, use
  [Query Contents](/docs/<link_to_Contents>)
  to get all Contents.
  Set `paging.limit` to 1000.

    If you receive 1,000 Contents, _____.

2. Upload the returned Contents to the external _____.

3. Save the current datetime, and use it in the next request.
  Each subsequent request
  needs to use the datetime of the request that came before it.

4. For all subsequent loads, use
  [Query Contents](/docs/<link_to_Contents>),
  and filter for new Contents created since the last load:

    ```json
    {
      "sort": {
        "fieldName": "createdDate",
        "order" : "ASC"
      },
      "filter": {
        "createdDate": {
          "$gt": "<PREVIOUS_LOAD_DATETIME>"
        }
      }
    }
    ```

5. Repeat steps 2 to 4 for each subsequent load.
  You can allow the site admin to configure the time interval with your app
  to fit their needs.
