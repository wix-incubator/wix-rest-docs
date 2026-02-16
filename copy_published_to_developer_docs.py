#!/usr/bin/env python3
"""
Script to copy published articles to developer-docs repository.
- Getting Started & Core Concepts → developer-docs/api-reference-articles
- Business Solutions & Product Articles → developer-docs/rest-docs
"""

import os
import shutil
from pathlib import Path

# Getting Started & Core Concepts - goes to api-reference-articles
GETTING_STARTED_ARTICLES = [
    "guides/Overview.md",
    "guides/Authentication.md",
    "guides/Identities.md",
    "guides/Permissions.md",
    "guides/API Query Language.md",
    "guides/Pagination.md",
    "guides/QueryVsSearch.md",
    "guides/Webhooks.md",
    "guides/DomainEvents.md",
    "guides/Errors.md",
    "guides/RateLimits.md",
    "guides/FQDNs.md",
    "guides/developer-preview.md",
    "guides/WixApps.md",
    "guides/Troubleshooting.md",
    "guides/DevGlossary.md",
    "guides/Data Payloads.md",
    "guides/SPI.md",
    "guides/APIVersions.md",
    "guides/App Versions.md",
    "guides/field-projection.md",
    "guides/ReleaseNotes.md",
    "guides/OverviewNew.md",
    "guides/CommonObjects.md",
    "guides/Deprecations.md",
    "guides/Create Your Wix App.md",
    # YAML config files for getting started
    "guides/getting-started.yaml",
    "guides/tutorials.yaml",
    "guides/what-is-new.yaml",
]

# Business Solutions & Product Articles - goes to rest-docs
BUSINESS_SOLUTION_ARTICLES = [
    # Wix Bookings
    "wix-bookings/guides/About Wix Bookings.md",
    "wix-bookings/guides/Terminology.md",
    "wix-bookings/guides/Sample App.md",
    "wix-bookings/guides/wix-bookings.yaml",
    
    # Wix Stores
    "wix-stores/guides/About Wix Stores.md",
    "wix-stores/guides/Pagination.md",
    "wix-stores/guides/Rich Text.md",
    "wix-stores/guides/Stores Schema for Wix Search.md",
    "wix-stores/guides/carts/Introduction.md",
    "wix-stores/guides/stores.yaml",
    
    # Contacts
    "contacts/guides/introduction.md",
    "contacts/guides/sample-flows.md",
    "contacts/guides/contacts.yaml",
    
    # Coupons
    "wix-coupons/guides/About Wix Coupons.md",
    "wix-coupons/guides/coupons.yaml",
    
    # Loyalty Program
    "wix-loyalty-program/guides/Introduction.md",
    "wix-loyalty-program/guides/Example Flows.md",
    "wix-loyalty-program/guides/loyalty-program.yaml",
    
    # Inbox
    "inbox/guides/Introduction.md",
    "inbox/guides/Example Flows.md",
    "inbox/guides/inbox.yaml",
    
    # Automations
    "wix-automations/guides/Introduction.md",
    "wix-automations/guides/Sample Flows.md",
    "wix-automations/guides/automations.yaml",
    
    # Wix Chat
    "wix-chat/guides/chat/Introduction.md",
    "wix-chat/guides/chat/chat.yaml",
    
    # App Management
    "app-management/guides/About App Management.md",
    "app-management/guides/About the Editor Deep Link API.md",
    "app-management/guides/Create an Editor Deep Link.md",
    "app-management/guides/app-instance/Introduction.md",
    "app-management/guides/app-management.yaml",
    "app-management/EmbeddedScriptSDK.md",
    
    # Wix Payments
    "wix-payments/guides/About Wix Payments.md",
    "wix-payments/guides/payments/About Payments.md",
    "wix-payments/guides/paymants.yaml",
    
    # Wix Cashier
    "wix-cashier/guides/AboutCashier.md",
    "wix-cashier/guides/cashier.yaml",
    
    # All Guides - Wix Events
    "all/guides/wix-events/Introduction.md",
    "all/guides/wix-events/About Wix Events.md",
    "all/guides/wix-events/Use Cases.md",
    "all/guides/wix-events/Rich Text.md",
    "all/guides/wix-events/Pagination.md",
    "all/guides/wix-events/Filter and Sort.md",
    "all/guides/wix-events/Fieldset.md",
    "all/guides/wix-events/Partial Updates.md",
    "all/guides/wix-events/Event/About the Events API.md",
    "all/guides/wix-events/Registration Form/About the Registration Form API.md",
    "all/guides/wix-events/events.yaml",
    
    # All Guides - Forum
    "all/guides/wix-forum/docs/intro.md",
    "all/guides/wix-forum/docs/filterAndSort.md",
    
    # All Guides - Groups
    "all/guides/wix-groups/docs/Introduction.md",
    "all/guides/wix-groups/docs/Terminology.md",
    "all/guides/wix-groups/docs/Flow.md",
    
    # All Guides - Wix Data
    "all/guides/wix-data/docs/WixDataServiceIntro.md",
    "all/guides/wix-data/docs/DataItemsServiceIntro.md",
    "all/guides/wix-data/docs/DataCollectionServiceIntro.md",
    "all/guides/wix-data/docs/Indexing.md",
    "all/guides/wix-data/docs/IndexTypes.md",
    "all/guides/wix-data/docs/IndexUseCases.md",
    "all/guides/wix-data/docs/IndexesAndQuerySpeed.md",
    "all/guides/wix-data/docs/EventualConsistency.md",
    "all/guides/wix-data/docs/ExternalDatabaseConnections.md",
    
    # All Guides - Stores Catalog
    "all/guides/stores-catalog/docs/intro.md",
    "all/guides/stores-catalog/docs/filterAndSort.md",
    "all/guides/stores-catalog/docs/ecom_integration.md",
    "all/guides/stores-catalog/docs/queryingProductAvailability.md",
    
    # All Guides - Stores Orders
    "all/guides/stores-orders/docs/intro.md",
    "all/guides/stores-orders/docs/filterAndSort.md",
    
    # All Guides - Stores Inventory
    "all/guides/stores-inventory/docs/intro.md",
    "all/guides/stores-inventory/docs/howToUse.md",
    
    # All Guides - Stores Carts
    "all/guides/stores-carts/docs/intro.md",
    
    # All Guides - Stores Abandoned Carts
    "all/guides/stores-abandoned-carts/docs/intro.md",
    "all/guides/stores-abandoned-carts/docs/use_case.md",
    
    # All Guides - Stores Subscription Options
    "all/guides/stores-subscription-options/docs/intro.md",
    "all/guides/stores-subscription-options/docs/example-flows.md",
    
    # All Guides - Media Manager
    "all/guides/site-media---media-manager-backend/docs/intro.md",
    "all/guides/site-media---media-manager-backend/docs/sample_flows.md",
    "all/guides/site-media---media-manager-backend/docs/upload_api.md",
    "all/guides/site-media---media-manager-backend/docs/resumable_upload_api.md",
    "all/guides/site-media---media-manager-backend/docs/import_files.md",
    
    # All Guides - Comments
    "all/guides/comments/docs/Introduction.md",
    "all/guides/comments/docs/USE_CASES.md",
    "all/guides/comments/docs/Sample_Flows.md",
    "all/guides/comments/docs/Sort_and_Filter.md",
    "all/guides/comments/docs/CONSUMERS.md",
    "all/guides/comments/docs/README.md",
    
    # All Guides - Email Subscriptions
    "all/guides/email-subscriptions/docs/intro.md",
    "all/guides/email-subscriptions/docs/example-flows.md",
    
    # All Guides - Payment Provider SPI
    "all/guides/payment-provider-spi/Provider Platform Overview.md",
    "all/guides/payment-provider-spi/Schema.md",
    "all/guides/payment-provider-spi/Authentication.md",
    "all/guides/payment-provider-spi/Response Error Object.md",
    "all/guides/payment-provider-spi/Reason Codes.md",
    
    # All Guides - Pricing Integration SPI
    "all/guides/pricing-integration-spi/docs/Intro.md",
    "all/guides/pricing-integration-spi/docs/SampleFlows.md",
    "all/guides/pricing-integration-spi/docs/BestPractices.md",
    
    # All Guides - Validations Integration SPI
    "all/guides/validations-integration-spi/docs/intro.md",
    "all/guides/validations-integration-spi/docs/sample-flow.md",
    
    # All Guides - Site Properties
    "all/guides/site-properties/docs/Introduction.md",
    "all/guides/site-properties/docs/README.md",
    
    # All Guides - Transactions
    "all/guides/transactions/doc/intro.md",
    "all/guides/transactions/doc/disputes.md",
    
    # All Guides - Wix Payments Transactions
    "all/guides/wix-payments-transactions/docs/intro.md",
    "all/guides/wix-payments-transactions/docs/disputes.md",
    
    # All Guides - Wix Forms
    "all/guides/wix-forms/Introduction.md",
    
    # All Guides - Wix Chat
    "all/guides/wix-chat/docs/intro.md",
    
    # All Guides - Social Groups V2
    "all/guides/social-groups-v2/docs/Introduction.md",
    
    # All Guides - Triggered Events
    "all/guides/triggered-events/docs/intro.md",
    "all/guides/triggered-events/docs/the-payload-schema.md",
    "all/guides/triggered-events/docs/reporting-and-canceling-events.md",
    
    # All Guides - TXT File Server
    "all/guides/txt-file-server/docs/PublicIntro.md",
    "all/guides/txt-file-server/docs/AdsTxt_PublicIntro.md",
    "all/guides/txt-file-server/docs/AdsTxt_Flow.md",
    
    # All Guides - Resellers
    "all/guides/resellers/docs/Intro.md",
    "all/guides/resellers/docs/Flow.md",
    "all/guides/resellers/docs/Errors.md",
    "all/guides/resellers/docs/SupportedFilters.md",
    
    # All Guides - Site Folders
    "all/guides/site-folders/docs/README-External.md",
    
    # All Guides - Bookings
    "all/guides/bookings---waitlist-service/API Overview.md",
    "all/guides/bookings---schedules-and-sessions/bookings-schedules-sessions.yaml",
    "all/guides/bookings---services/bookings-services.yaml",
    "all/guides/bookings---service-catalog/docs/bookings-service-catalog.yaml",
    "all/guides/bookings---bookings-service/com/wix/bookings/api/v1/docs/bookings.yaml",
    "all/guides/bookings---checkout-service/checkout-options.yaml",
    "all/guides/bookings---external-calendar-sync/external-calendar-sync.yaml",
    
    # All Guides - FAQ
    "all/guides/faq/docs/faq.yaml",
    
    # Account Level APIs
    "account-level-apis/guides/account-level-apis.yaml",
]

def copy_files_to_destination(source_root, files_list, dest_root, category_name, dry_run=False):
    """
    Copy files from source to destination.
    
    Returns: (copied_count, missing_count, error_count)
    """
    source_path = Path(source_root)
    dest_path = Path(dest_root)
    
    copied = 0
    missing = 0
    errors = 0
    
    print(f"\n{'=' * 80}")
    print(f"COPYING: {category_name}")
    print(f"{'=' * 80}")
    print(f"Destination: {dest_path}")
    print(f"Files to copy: {len(files_list)}")
    print(f"{'=' * 80}\n")
    
    for rel_path in files_list:
        source_file = source_path / rel_path
        dest_file = dest_path / rel_path
        
        if not source_file.exists():
            print(f"[MISSING] {rel_path}")
            missing += 1
            continue
        
        if dry_run:
            print(f"[WOULD COPY] {rel_path}")
            copied += 1
        else:
            try:
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_file, dest_file)
                print(f"[COPIED] {rel_path}")
                copied += 1
            except Exception as e:
                print(f"[ERROR] {rel_path}: {e}")
                errors += 1
    
    print(f"\n{category_name} Summary:")
    print(f"  Copied: {copied}")
    print(f"  Missing: {missing}")
    print(f"  Errors: {errors}")
    
    return copied, missing, errors

def create_manifest(dest_root, files_list, category_name):
    """Create a manifest file listing all copied files."""
    dest_path = Path(dest_root)
    manifest_path = dest_path / f"MANIFEST_{category_name.replace(' ', '_').upper()}.md"
    
    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.write(f"# {category_name} - Manifest\n\n")
        f.write(f"This directory contains published {category_name.lower()} from wix-rest-docs.\n\n")
        f.write(f"**Total Files:** {len(files_list)}\n\n")
        
        f.write("## Files\n\n")
        for article in sorted(files_list):
            f.write(f"- {article}\n")
    
    print(f"✅ Created manifest at {manifest_path}")

def main():
    import sys
    
    # Default paths
    source_root = "."
    api_reference_dest = "developer-docs/api-reference-articles"
    rest_docs_dest = "developer-docs/rest-docs"
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    
    # Allow custom paths from command line
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        source_root = sys.argv[1]
    if len(sys.argv) > 2 and not sys.argv[2].startswith("--"):
        api_reference_dest = sys.argv[2]
    if len(sys.argv) > 3 and not sys.argv[3].startswith("--"):
        rest_docs_dest = sys.argv[3]
    
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║          WIX PUBLISHED ARTICLES → DEVELOPER-DOCS COPY TOOL                ║
╚═══════════════════════════════════════════════════════════════════════════╝

This script will copy published articles to two destinations:
  1. Getting Started & Core Concepts → developer-docs/api-reference-articles
  2. Business Solutions & Products  → developer-docs/rest-docs

""")
    
    print(f"Source: {source_root}")
    print(f"Destination 1: {api_reference_dest} ({len(GETTING_STARTED_ARTICLES)} files)")
    print(f"Destination 2: {rest_docs_dest} ({len(BUSINESS_SOLUTION_ARTICLES)} files)")
    print(f"Total files: {len(GETTING_STARTED_ARTICLES) + len(BUSINESS_SOLUTION_ARTICLES)}")
    print(f"Dry run: {dry_run}\n")
    
    # Confirm with user unless it's a dry run
    if not dry_run:
        response = input("Continue? [y/N]: ")
        if response.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)
    
    # Copy getting started articles
    gs_copied, gs_missing, gs_errors = copy_files_to_destination(
        source_root, 
        GETTING_STARTED_ARTICLES, 
        api_reference_dest,
        "Getting Started & Core Concepts",
        dry_run
    )
    
    # Copy business solution articles
    bs_copied, bs_missing, bs_errors = copy_files_to_destination(
        source_root,
        BUSINESS_SOLUTION_ARTICLES,
        rest_docs_dest,
        "Business Solutions & Products",
        dry_run
    )
    
    # Overall summary
    total_copied = gs_copied + bs_copied
    total_missing = gs_missing + bs_missing
    total_errors = gs_errors + bs_errors
    total_files = len(GETTING_STARTED_ARTICLES) + len(BUSINESS_SOLUTION_ARTICLES)
    
    print(f"\n{'=' * 80}")
    print(f"OVERALL SUMMARY")
    print(f"{'=' * 80}")
    print(f"Total copied: {total_copied}/{total_files}")
    print(f"Missing files: {total_missing}")
    print(f"Errors: {total_errors}")
    print(f"{'=' * 80}\n")
    
    if total_missing > 0:
        print("⚠️  Some files were not found in the source repository.")
    
    if total_errors > 0:
        print("❌ Some files failed to copy. Check the errors above.")
    
    if total_copied > 0 and not dry_run:
        print(f"✅ Successfully copied {total_copied} published articles!")
        
        # Create manifests
        create_manifest(api_reference_dest, GETTING_STARTED_ARTICLES, "Getting Started")
        create_manifest(rest_docs_dest, BUSINESS_SOLUTION_ARTICLES, "Business Solutions")
    
    print("\n✨ Done!")

if __name__ == '__main__':
    main()
