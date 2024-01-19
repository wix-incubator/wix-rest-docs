SortOrder: 1
# Sample Flows

This article shares some possible use cases your app could support, as well as a sample flow that could support each use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.

## Backing up data before a major update

Suppose your app is about to update many items in a site's collections. For example, it is updating inventory with the most recent stock quantities in a store. Before such a major update, your app can back up site data as follows:

1. Use [Create Backup]() to generate a new on-demand backup of all live content in a Wix site's data collections.

2. To check whether the new backup has been completed successfully, use [List Backups](). A completed backup's `status` property has the value `READY`. This means it can be used to restore the site's data.

3. Continue [managing site data]() as usual. In most cases, you shouldn't need the later steps!

## Restoring data from a backup

What if a site owner accidentally entered incorrect data? For example, suppose they inadvertently provided figures from the wrong month. Your app can provide the option of reverting site data to a prior state as follows:

1. To restore site data from a backup, you first need to choose which backup to restore.

    Use [List Backups]() with the `status` parameter value `READY` to retrieve a list of all backups that can be used for a restoration, ordered from newest to oldest.

    You need the ID of the backup you wish to restore data from. If you wish to restore data from the most recent backup, save the ID of the first backup in the list.

2. Use [Restore Backup]() with the ID of the backup you wish to restore data from.

3. To check whether the data restoration has been completed successfully, use [List Restorations](). A completed restoration's `status` property has the value `COMPLETED`. This means the content of site collections has reverted to its state at the time of the selected backup.

4. After restoring data from a backup, you may wish to delete the backup you restored from. This way, you can retain older backups which may have been created at important junctures, while also freeing a slot for a new backup. To do this, use [Delete Backup]() with the ID of the backup you restored data from.