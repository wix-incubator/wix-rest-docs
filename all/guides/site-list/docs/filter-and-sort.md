SortOrder: 1
## Filter

Both the Query Sites and Count Sites endpoints accept the following filters:
* id
  ```
  { id: { $in: ['015c25c0-24e8-4966-a951-a3b458da7351', '04067d48-5b6c-48b5-9c08-8397d7e8d53a'] } }
  ```
* folderId
    * filter sites that are in root level (no folder):
      ```
      { folderId: { $exists: false } }
      ```
    * filter sites that are in a specific folder:
      ```
      { folderId: '54915d80-62c2-4791-8483-88541ed18a60' }
      ```
* editorType
  ```
  { editorType: 'EDITOR' }
  ```
* appIds
    * filter sites that have provided app ids:
      ```
      { appIds: { $hasAll: ['1dbbce47-77b4-4ccf-be8c-8434eab7f58d', '87beaf91-cf01-4209-93ed-eb7cc47dc2cf' ] } }
      ```
    * filter sites that have at least one of the provided app ids:
      ```
      { appIds: { $hasSome: ['1dbbce47-77b4-4ccf-be8c-8434eab7f58d', '87beaf91-cf01-4209-93ed-eb7cc47dc2cf' ] } }
      ```
* premium
    ```
    { premium: true }
    ```
* published
  ```
  { published: true }
  ```
* namespace
  ```
  { namespace: 'WIX' }
  ```
* name (the same as `searchPhrase` filter. Searches in name, display name and domains)
  ```
  { name: 'my-site' }
  ```
* searchPhrase (the same as `name` filter. Searches in name, display name and domains)
  ```
  { searchPhrase: 'my-site' }
  ```
* state
  ```
  { state: 'ACTIVE' }
  ```
* domainConnected
  ```
  { domainConnected: true }
  ```

## Sort

Sorting can be specified by the following fields:
* createdDate
  ```
  { fieldName: 'createdDate', order: 'ASC' }
  ```
* trashedDate
  ```
  { fieldName: 'trashedDate', order: 'DESC' }
  ```
* updatedDate
  ```
  { fieldName: 'updatedDate', order: 'ASC' }
  ```
* displayName
  ```
  { fieldName: 'displayName', order: 'DESC' }
  ```
