SortOrder: 0
# **About this API**
An Album is a responsive, customizable site created as part of the main photographer site, used to display galleries containing high quality media.

# **Terminology**
**Album** - represent an Album instance. An Album can have galleries and Cover photo in it.

**Gallery** - represent a ProGallery instance. A Gallery can have Items in it.

**Item** can be a Photo/ Video/ Text Item.

**State** -  an Album also has State which indicates whether the album is:

- Saved: the given album in the Editor segment
- Published: the given album in the LiveSite segment

For example:
A user can edit his album in the editor, without publishing it. in this case, only the album in SAVED state is to be updated.
When the album is published, the changes made in the editor will apply to the album in PUBLISHED state. 

