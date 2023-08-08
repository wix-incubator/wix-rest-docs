SortOrder: 0
# Comments Context Provider SPI

Server Infra SPI
documentation - [link](https://github.com/wix-private/server-infra/blob/master/framework/loom/spi-client/README.md#service-provider-interface-spi)

Comment Context Provider allows each product to enhance and customise functionality of Comments API. Each vertical can
customise permission model by providing different set of permissions for each member or visitor individually per
context.
Provider can also provide details about resources comments pertain to, this helps to ease management of comments in
Business Manager.

If 3rd party want to fetch context permissions for Blog Comments, they are not required to implement this SPI as this is
already done by Wix Blog backend.
Although if they want to be able to configure permissions of particular context that lives in their app, they must
implement it. There's no default implementation.

## Terminology

* Context - the environment in which a comment is being made. For instance, if a
  Comments API is being used on an e-commerce website, the context of a comment could be the specific
  product page on which the comment was made. This context helps determine things like who can see the comment, who can
  create comment, who can reply to the comment.
* Resource - in a Comments API refers to any object that comments can be assigned to from the context. For example, in
  the context of a blog post, the blog post itself would be a resource
* Comments Environment - describes the specific environment in which the comment functionality is operating.
    * Live Site - handles comments created by UoU - Members or Visitors
    * Business Manager - handles comments created by Wix User

## Limitations

* Each Vertical can implement Comments Context Provider once.  