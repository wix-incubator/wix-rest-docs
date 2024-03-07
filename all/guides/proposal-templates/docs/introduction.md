SortOrder: 0
# About Proposals

Proposals is a product in Get Paid group of products that allows users (Site collaborators with required permissions) to create a 
business proposal/contract that can be shared with their clients to agree on and arrange business opportunities.

Users can specify items comprising their proposal, item pricing and other financial details and can also use proposal editor provided by 
third party provider to define business contract.

Proposals API provides capabilities to:
- Manage (create, read, update, delete, set status) proposals
- Send proposals to predefined contacts
- Query proposal templates from the proposal editor provider (via SPI implementation)

Proposal editor provider is also expected to use this API during some flows to notify of changes happening on the provider part of flows

## Before you begin

Proposals product has dependencies on other products and also on proposal editor provider, as a result InitializeProposals endpoint should be called 
once per site. This endpoint ensures that Proposals and eCom application is installed in the site and also marks the site as having provided 
consent to share site data with proposal editor provider.

## Use cases

[//]: # (> List **use cases** for your API in this section.)
[//]: # (> This section is a simple bullet list.)
[//]: # (>)
[//]: # (> Make sure to cover REST, Velo, and SDK use cases.)
[//]: # (>)
[//]: # (> This helps your tech writer better understand your API)
[//]: # (> and ensures smoother design review and documentation process.)
[//]: # (>)
[//]: # (> **Remember**:)
[//]: # (> Your audience is a developer who isn't familiar with your API and product.)
[//]: # (>)
[//]: # (> Delete this note when you're done.)

TODO

## Terminology

- **Proposal editor provider**: third party app that provides capability to edit visual representation of proposal and also implements ProposalEditorProvider SPI
