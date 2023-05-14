SortOrder: 6
# Namespaces - Media Manager multi tenancy/partitions

Namespaces is a param that is available in most request made to the "Site Media"

This param is used for internal verticals to create their own "partition" in the media manager

The media manager dialog can be open with a specific namespace - to display files only related to this namespace.

For example: Wix Stores use their own namespace so that digital goods are available only when opening the media manager from stores.

Actions made with a namespace param like "empty trashbin", "list files" and others, will only work on files related to the namespace provided in that request.
