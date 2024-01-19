SortOrder: 0
# About the Backups API

The Backups API enables your app to create and manage backups of the live content in a Wix site's collections.

With Backups, your app can:
- Create a backup of data in a Wix site's collections.
- [Restore data](#restore-backup) from an existing backup.
- Retrieve information about prior and ongoing backups and restorations.

Backups enable you to restore a Wix site's collections' content in the event of data corruption, erroneous deletions, or other mistakes.

The system creates a backup automatically every 7 days. In addition, you can use the Backups API to create an on-demand backup when significant changes are made to your data. For example:
- If an automated backup is not scheduled soon, create an on-demand backup after updating your data, to ensure your new content is backed up as soon as possible.
- Create an on-demand backup prior to a major update to a Wix site's collections, so you can restore your most recent pre-update data in the event something goes wrong during the update.

For information on how site owners can back up the content of a Wix site's collections using the Content Manager, see [Backing Up Your Collections](https://support.wix.com/en/article/content-manager-backing-up-your-collections).

## Before you begin

It's important to note the following points before starting to code:
- Backups include only live content. They don't include content contained in the optional [sandbox](https://support.wix.com/en/article/content-manager-about-sandbox-and-live-collections-and-syncing).
- Backups include only collection content. They don't store a collection's schema or named views.
- A site can store a maximum of 3 on-demand backups. If 3 on-demand backups already exist and you create a new backup, the oldest existing on-demand backup is deleted.
- When you restore data from a backup, the restoration process replaces the collection's current data with the data in the backup. So if you add items to a collection after initiating a backup, and then you restore data from that backup, the new content may be lost.
- If any content is submitted to a collection during the restoration process, that content may be lost.

## Terminology

- **Backup:** A full copy of the live content contained in a Wix site's collections.
    - **Auto:** A backup taken automatically by the system on a regular schedule.
    - **On demand:** A backup initiated manually.
- **Restoration:** Regeneration of a Wix site's collection content from a prior backup.