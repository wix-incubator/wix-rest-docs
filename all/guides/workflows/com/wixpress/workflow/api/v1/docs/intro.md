SortOrder: 0
# About Workflows

With [Workflows](https://support.wix.com/en/article/workflows-getting-started),
site owners can manage their customer relationship management processes.
Site owners can use workflows to track leads, contacts, orders, and more
on a kanban-style board.

Workflow boards are separated into phases
that represent steps in a project, process or flow.
Workflows are contact-based,
meaning each card has an attached contact,
giving a visual indicator of where the contact stands
and what needs to be done next.

The Workflows API contains functionality
that allows your app to read and manage workflows, phases, and cards.
With the Workflows API, your app can keep statuses in sync with an external tool.

Read more on how site owners can
[use Workflows to streamline their business processes][kb-workflows-getting-started].

## Terminology

- A **workflow** is a board that defines a process.
  A site can contain up to 30 workflows.
- A **phase** (called a **step** in the Dashboard) is a stage of the workflow.
- A workflow contains up to 60 **active phases**,
  which are used to  and a **win phase**.
- A **card** represents a tracked item related to a
  [site contact][contacts-api].
  Cards can be moved along the workflow phases.
- If a card is in an active phase, it's an **active card**.
  If a card is in the win phase or archived, it's not an active card.
  A workflow can contain up to 5,000 active cards.

[active-vs-completed]: planning-your-app.md
[kb-workflows-getting-started]: https://support.wix.com/en/article/workflows-getting-started
[contacts-api]: https://dev.wix.com/api/rest/contacts/contacts/introduction
