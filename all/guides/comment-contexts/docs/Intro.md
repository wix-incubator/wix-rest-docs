SortOrder: 0
# Introduction

Comment Context provides a way to get details about available application that uses

Comment Context Service is service which provides details about Comment API consumers. It provides information about
how the API is used and gives callers the ability to find out what actions they can do in different contexts. Service
also allows applications to get more information about the resources connected to the comments.

## Terminology

* App - application that is installed in current site and are providing comment context
* Context - the environment in which a comment is being made. For instance, if a Comments API is being used on an
  e-commerce website, the context of a comment could be the specific product page on which the comment was made. This
  context helps determine things like who can see the comment, who can create comment, who can reply to the comment.
* Resource - in a Comments API refers to any object that comments can be assigned to from the context. For example, in
  the
  context of a blog post, the blog post itself would be a resource
* Comments Environment - describes the specific environment in which the comment functionality is operating.
    * Live Site - handles comments created by UoU - Members or Visitors
    * Business Manager - handles comments created by Wix User