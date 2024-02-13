SortOrder: 2
# Catalog SPI: Sample Use Cases & Flows

This article presents sample flows your app can support. You aren't limited to this exact flow, but it can be a helpful jumping off point as you plan your catalog integration.

## Add a catalog item to a cart

> **Note:** In this example, item variant details are passed in the request. Learn more about this approach to [handling item variants](./Catalog-Reference.md#approach-1--pass-variant-details-in-options).

In this flow, a site visitor adds an item to their cart. Wix calls the Catalog SPI to retrieve the item's full details. Before implementing this flow, [configure your app](./Introduction.md#configuration) so it can communicate with your Catalog SPI implementation.

1. A site visitor selects a color and size for a customizable T-shirt on a Wix site's item page. Then they add it to their cart.

1. The app code calls [Create Cart](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/cart/create-cart) with the following `lineItems` array in the payload to create a new cart that includes the item:

    ```json
    {
      "lineItems": [
        {
          "quantity": 1,
          "catalogReference": {
            "appId": "3b8658a6-3282-4b5e-ae0e-439113e20aef",
            "catalogItemId": "f95bd723-ea83-40f2-8cb8-accff2d54866",
            "options": {
              "color": "Green",
              "size": "M"
            }
          }
        }
      ]
    }
    ```

    The `catalogReference` object for the item includes:

    + `appId`: The ID of the app the catalog belongs to. This tells Wix which app's implementation of the Catalog SPI to call.
    + `catalogItemId`: The ID of the item in the catalog it belongs to.
    + `options`: Item variant information.

    In this case, the app handles item variants by passing the variant details in the `catalogReference` object's `options` field.

1. Wix automatically calls your app's implementation of [Get Catalog Items](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/catalog-spi/get-catalog-items) with the following payload to retrieve the item's full and current details:

    ```json
    {
      "catalogReferences": [
        {
        "catalogReference": {
          "appId": "3b8658a6-3282-4b5e-ae0e-439113e20aef",
          "catalogItemId": "f95bd723-ea83-40f2-8cb8-accff2d54866",
          "options": {
            "color": "Green",
            "size": "M"
          }
        },
        "quantity": 1
        }
      ],
      "currency": "USD",
      "weightUnit": "KG"
    }
    ```

1. Your implementation of Get Catalog Items returns a response like this one:

    ```json
    {
      "catalogItems": [
        {
          "catalogReference": {
            "appId": "3b8658a6-3282-4b5e-ae0e-439113e20aef",
            "catalogItemId": "f95bd723-ea83-40f2-8cb8-accff2d54866",
            "options": {
              "color": "Green",
              "size": "M"
            }
          },
          "data": {
            "productName": {
              "original": "Cotton T-shirt"
            },
            "url": {
              "relativePath": "/product-page/t-shirt",
              "url": "https://www.<MY_STORE>.com/"
            },
            "itemType": {
              "preset": "PHYSICAL"
            },
            "price": {
              "amount": "80.00"
            },
            "descriptionLines": [
              {
                "name": {
                  "original": "Size",
                  "translated": "Size"
                },
                "plainText": {
                  "original": "Medium",
                  "translated": "Medium"
                }
              },
              {
                "name": {
                  "original": "Color",
                  "translated": "Color"
                },
                "plainText": {
                  "original": "Green",
                  "translated": "Green"
                }
              }
            ],
            "physicalProperties": {
              "sku": "889809004958",
              "shippable": true
            },
            "media": {
              "id": "3258d9_77f175cc4d234714825fbf316803ca9a~mv2.png",
              "height": 720,
              "width": 720
            }
          }
        }
      ]
    }    
    ```

    It's important to note the following about the response:
    + The `catalogReference` object in the response must be identical to the one received in the request.
    + The response must include the variant details associated with the preferences specified in `options`.
    + The response must include all fields marked as required in the [response description](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/catalog-spi/get-catalog-items).

1. Wix adds the item to the visitor's cart, including the name, price, image, and variant details.

## Add a catalog item to a checkout

> **Note:** In this example, item variant details are processed externally via a custom API that returns a unique ID. Learn more about this approach to [handling item variants](./Catalog-Reference.md#approach-2--pass-a-variant-id-in-options).

In this flow, a site visitor adds an item to their checkout. Wix calls the Catalog SPI to retrieve the item's full details. Before implementing this flow, [configure your app](./Introduction.md#configuration) so it can communicate with your Catalog SPI implementation.

1. A site visitor selects a color and size for a customizable T-shirt on a Wix site's item page. Then they click **Buy Now** to add it directly to their checkout.

1. The app code calls a custom API with the variant details. The custom API validates and stores these details, then returns a unique `variantId`.

1. The app code calls [Create Checkout](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/checkout/create-checkout) with the following `lineItems` array in the payload to create a new checkout that includes the item:

    ```json
    {
      "lineItems": [
        {
          "quantity": 1,
          "catalogReference": {
            "appId": "3b8658a6-3282-4b5e-ae0e-439113e20aef",
            "catalogItemId": "f95bd723-ea83-40f2-8cb8-accff2d54866",
            "options": {
              "variantId": "c1988f6b-00a6-4e24-bd60-ce3054a54fbd"
            }
          }
        }
      ]
    }
    ```

    The `catalogReference` object for the item includes:

    + `appId`: The ID of the app the catalog belongs to. This tells Wix which app's implementation of the Catalog SPI to call.
    + `catalogItemId`: The ID of the item in the catalog it belongs to.
    + `options`: Item variant information.

    In this case, the app handles item variants by using a custom API to generate and store the variant details. It then passes only the variant ID details in the `catalogReference` object's `options` field.

1. Wix automatically calls your app's implementation of [Get Catalog Items](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/catalog-spi/get-catalog-items) with the following payload to retrieve the item's full and current details:

    ```json
    {
      "catalogReferences": [
        {
        "catalogReference": {
          "appId": "3b8658a6-3282-4b5e-ae0e-439113e20aef",
          "catalogItemId": "f95bd723-ea83-40f2-8cb8-accff2d54866",
          "options": {
            "variantId": "c1988f6b-00a6-4e24-bd60-ce3054a54fbd"
          }
        },
        "quantity": 1
        }
      ],
      "currency": "USD",
      "weightUnit": "KG"
    }
    ```

1. Your implementation of Get Catalog Items returns a response like this one:

    ```json
    {
      "catalogItems": [
        {
          "catalogReference": {
            "appId": "3b8658a6-3282-4b5e-ae0e-439113e20aef",
            "catalogItemId": "f95bd723-ea83-40f2-8cb8-accff2d54866",
            "options": {
              "color": "Green",
              "size": "M"
            }
          },
          "data": {
            "productName": {
              "original": "Cotton T-shirt"
            },
            "url": {
              "relativePath": "/product-page/t-shirt",
              "url": "https://www.<MY_STORE>.com/"
            },
            "itemType": {
              "preset": "PHYSICAL"
            },
            "price": {
              "amount": "80.00"
            },
            "descriptionLines": [
              {
                "name": {
                  "original": "Size",
                  "translated": "Size"
                },
                "plainText": {
                  "original": "Medium",
                  "translated": "Medium"
                }
              },
              {
                "name": {
                  "original": "Color",
                  "translated": "Color"
                },
                "plainText": {
                  "original": "Green",
                  "translated": "Green"
                }
              }
            ],
            "physicalProperties": {
              "sku": "889809004958",
              "shippable": true
            },
            "media": {
              "id": "3258d9_77f175cc4d234714825fbf316803ca9a~mv2.png",
              "height": 720,
              "width": 720
            }
          }
        }
      ]
    }    
    ```

    It's important to note the following about the response:
    + The `catalogReference` object in the response must be identical to the one received in the request.
    + The response should include the variant details associated with the `variantID` provided in `options`.
    + The response must include all fields marked as required in the [response description](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/catalog-spi/get-catalog-items).

1. Wix adds the item to the visitor's checkout, including the name, price, image, and variant details.
