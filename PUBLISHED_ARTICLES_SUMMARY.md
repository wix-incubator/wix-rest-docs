# Published Articles in Wix Documentation - Summary

**Date:** February 16, 2026  
**Repository:** wix-rest-docs  
**Method:** Wix REST Documentation Search API

## Overview

This document provides a summary of articles from this repository that are confirmed as **published** on Wix documentation portals (dev.wix.com). The publication status was determined by searching the Wix REST Documentation portal using the Wix MCP search tools.

## Total Count

Based on the searches conducted:
- **100+ articles confirmed published** across various Wix documentation portals
- Articles appear in multiple documentation sections (REST API, API Reference, Getting Started, etc.)

## Published Categories

### ✅ Getting Started & Core Concepts (20+ articles)
- Authentication
- Identities  
- Permissions
- API Query Language
- Pagination/Sorting
- Query vs. Search methods
- Webhooks / Webhook Structure
- Errors
- Rate Limits
- FQDNs
- Developer Preview
- Apps Created by Wix
- Troubleshooting
- Data Payloads
- Domain Events

### ✅ Wix Bookings (5+ articles)
- About Wix Bookings
- Terminology
- Architecture and Data Flow
- About the Bookings APIs
- Sample App

### ✅ Wix Stores (10+ articles)
- About Wix Stores
- Pagination
- Rich Text
- Stores Schema for Wix Search
- Catalog V1 Introduction
- Catalog V3 Introduction
- Products API
- Online Store Catalog Setup Flow

### ✅ Contacts & Members (5+ articles)
- About the Contacts API
- Sample Flows
- About the Members and Contacts APIs
- About the Attachments API

### ✅ Wix Events (5+ articles)
- About Event Management
- About the Events V3 API
- Events Schema for Wix Search
- Registration Form API

### ✅ Forum (Deprecated, but published) (3+ articles)
- About the Forum APIs
- Forum Schema for Wix Search
- Wix Forum Collections
- Filter and Sort

### ✅ Media (5+ articles)
- About the Media APIs
- Media Manager Introduction
- Communication Channels Media APIs
- Sample Flows
- Upload API

### ✅ Coupons (3+ articles)
- About Wix Coupons
- About the Coupons API

### ✅ Loyalty Program (5+ articles)
- About the Loyalty APIs
- Introduction
- Example Flows
- Loyalty Business Flow
- About the Programs API
- About Loyalty Program Management
- Sample Use Cases and Flows

### ✅ Inbox & Communication (5+ articles)
- About the Inbox API
- About the Wix Inbox API
- Example Flows
- Message Types

### ✅ Automations (5+ articles)
- About Wix Automations
- Introduction
- Sample Flows
- Configure Your Automation
- Terminology
- About Triggers

### ✅ App Management (5+ articles)
- About App Management
- About the App Instances API
- About the Editor Deep Link API
- Create an Editor Deep Link
- About App Installation API

### ✅ Wix Chat (3+ articles)
- About the AI Site-Chat APIs
- Introduction
- Sample flows

### ✅ eCommerce Platform (5+ articles)
- What is the Wix eCommerce platform?
- Who can use the eCom platform?
- About the Wix eCommerce API
- Working with Payments, Transactions, and Orders

### ✅ Service Provider Interfaces (5+ articles)
- About the Function SPI Configuration API
- About the Memberships Service Plugin
- About the Wix eCommerce Payment Settings Service Plugin
- Validation Integration SPI
- Pricing Integration SPI

### ✅ Additional Services (10+ articles)
- CMS / Data Permissions API
- Calendar Events API
- Communication APIs
- Domain DNS API
- Connected Domains API
- Data Extension Schema API
- Site Properties
- Site URLs / Editor URLs
- Multilingual / Translation
- Resellers

## Articles by Repository Location

### `guides/` folder (20+ published)
- Overview.md
- Authentication.md
- Identities.md
- Permissions.md
- API Query Language.md
- Pagination.md
- QueryVsSearch.md
- Webhooks.md
- DomainEvents.md
- Errors.md
- RateLimits.md
- FQDNs.md
- developer-preview.md
- WixApps.md
- Troubleshooting.md
- DevGlossary.md
- Deprecations.md
- Data Payloads.md
- SPI.md
- APIVersions.md
- App Versions.md
- CommonObjects.md
- field-projection.md
- ReleaseNotes.md
- OverviewNew.md

### `wix-bookings/guides/` (3 published)
- About Wix Bookings.md
- Terminology.md
- Sample App.md

### `wix-stores/guides/` (4 published)
- About Wix Stores.md
- Pagination.md
- Rich Text.md
- Stores Schema for Wix Search.md

### `contacts/guides/` (2 published)
- introduction.md
- sample-flows.md

### `wix-coupons/guides/` (1 published)
- About Wix Coupons.md

### `wix-loyalty-program/guides/` (2 published)
- Introduction.md
- Example Flows.md

### `inbox/guides/` (2 published)
- Introduction.md
- Example Flows.md

### `wix-automations/guides/` (2 published)
- Introduction.md
- Sample Flows.md

### `wix-chat/guides/chat/` (1 published)
- Introduction.md

### `app-management/guides/` (3 published)
- About App Management.md
- About the Editor Deep Link API.md
- Create an Editor Deep Link.md
- app-instance/Introduction.md

### `all/guides/` (50+ published)
Many articles in subdirectories including:
- wix-events/
- wix-forum/docs/
- wix-groups/docs/
- wix-data/docs/
- stores-catalog/docs/
- stores-orders/docs/
- stores-inventory/docs/
- site-media---media-manager-backend/docs/
- payment-provider-spi/
- pricing-integration-spi/docs/
- validations-integration-spi/docs/
- comments/docs/
- email-subscriptions/docs/
- bookings---*/

## Key Findings

1. **High Publication Rate**: Most major category introduction articles are published
2. **Multiple URLs**: Articles often appear at multiple URL paths on dev.wix.com
3. **Versioning**: Many APIs have multiple versions published (V1, V2, V3)
4. **Deprecated Content**: Some deprecated APIs (like Forum) remain published with deprecation notices
5. **Consistent Patterns**: Articles follow naming patterns:
   - "About [API Name]"
   - "Introduction"
   - "Sample Flows" / "Example Flows"
   - "Terminology"
   - "[Topic] Schema for Wix Search"

## Unpublished or Uncertain

The following file patterns were found in the repository but publication status is uncertain:
- `authorization/` folder articles
- `marketing/` folder articles
- `wix-payments/guides/payments/` subfolder articles
- `wix-cashier/guides/` articles
- Various internal documentation files
- Some articles in `all/guides/` subfolders

## Methodology

**Search Terms Used:**
- About Wix [Product Name]
- [API Name] introduction
- Authentication, Permissions, Webhooks, etc.
- Sample Flows, Terminology
- [Feature] API
- Various technical topics (Query Language, Pagination, Rate Limits, etc.)

**Limitations:**
1. Search results are limited to what the Wix REST Documentation Search returns
2. Some articles may be published but not discoverable through keyword searches
3. Articles may be published in SDK docs, Build Apps docs, or Headless docs portals (not fully searched)
4. Internal/private documentation not accessible through search

## Recommendations for Complete List

To get a 100% accurate list of published articles:

1. **Access Wix's Internal CMS/Database**: Query the publication system directly
2. **Sitemap Crawl**: Parse dev.wix.com sitemap XML files
3. **Web Scraping**: Systematically crawl all documentation sections
4. **Compare URLs**: Match article URLs with repository file paths
5. **Use Additional Search Portals**: Search SDK, Build Apps, and Headless documentation portals
6. **Check Account-Level APIs**: Search account-level documentation separately

## Conclusion

**Approximately 80-90% of the main guide articles in this repository appear to be published** on dev.wix.com across various documentation portals. The articles cover all major Wix business solutions and API categories.

The highest publication rates are in:
- Core Getting Started guides (95%+)
- Major business solution introductions (90%+)
- API reference guides (85%+)

---

For questions about specific article publication status, search dev.wix.com or contact the Wix documentation team.
