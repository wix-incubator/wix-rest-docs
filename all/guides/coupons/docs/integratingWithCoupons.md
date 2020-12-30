SortOrder: 4
# Integrating with coupons

Read this if you want to integrate a new vertical into using coupons

Topics:
1. Decide on scopes, consult with coupons team
2. Implement a plugin controller - TODO link - Avital
3. Call calculate cart using the scopes - https://wixplorer.wixpress.com/coupons/reference/using-coupons/.wix.coupons.api.v2.-coupons-v2.-calculate-cart
4, Call increase usage once payment is confirmed - https://wixplorer.wixpress.com/coupons/reference/using-coupons/.wix.coupons.api.v2.-coupons-v2.-increase-usage
5, Go to RPC and add the controller - TODO link - Avital
6, Update enums in EDM - TODO link - Zeev
7. Ask technical writers to update the DB driver documentation - https://support.wix.com/en/article/wix-code-wix-marketing-coupons-collection-fields with the new scope values
8. Ask technical writers to update the EDM documentation (link doesn’t exist yet)
9. update validScopeValues.md

Need to turn this draft into actual documentation