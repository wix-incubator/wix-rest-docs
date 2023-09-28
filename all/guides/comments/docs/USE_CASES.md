SortOrder: 1
# Use Cases

### Export Blog comments to make most reacted widget elsewhere on site

If a site owner wants to manage blog comments on an external site to promote a blog, using REST API to copy comments to
their system should be used. To do this, external app can follow this basic flow to export most reacted comments:
Use Comment Query API to get list of 10 published comments sorted by most reactions

```json
{
  "appId": "14bcded7-0066-7c35-14d7-466cb3f09103",
  "query": {
    "filter": {
      "status": "PUBLISHED"
    },
    "sort": [
      {
        "fieldName": "reactionSummary.total",
        "order": "DESC"
      }
    ],
    "cursorPaging": {
      "limit": 10
    }
  }
}
```

Upload the returned comments to the external site to promote the blog in other pages.

There are similar Query Comments flow examples where it is allowed to export comments and filter or sort it by rating,
reactions, upvotes/downvotes, maybe sort exact blog post comments and upload it to the external site. The usage could be
to have it as a testimonial widget, use data to analyze received comments data or any other relevant to business. 
