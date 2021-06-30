SortOrder: 2
# Message Types

Messages can be sent as different types,
allowing for the display to match the message payload.
Your app can send messages as `PLAIN`, `TEMPLATE`, `MINIMAL`, or `FORM` type.
You may see an additional `CUSTOM` type in some responses.
`CUSTOM` type is reserved for internal use.

This article gives a brief overview of each of the message types.

## Plain Messages

`PLAIN` messages contain an array of `data` types.
Each `data` type can be `text`, `image`, or `file`.
Array items are displayed in Inbox and the visitor's chat widget
as if each item was a separate message with a separate payload.

This example payload's `data` array contains an image followed by two text messages:

```json
{
  "message": {
    "payload": {
      "type": "PLAIN",
      "summary": "Thanks for booking your spa day with us!",
      "plain": {
        "data": [
          {
            "type": "IMAGE",
            "image": {
              "url": "https://static.wixstatic.com/media/f93e3d633e79921f14330f1911fc1139.jpg/v1/fill/w_1200,h_798,al_c,q_85,usm_0.66_1.00_0.01/f93e3d633e79921f14330f1911fc1139.webp"
            }
          },
          {
            "type": "TEXT",
            "text": "Thanks for booking your spa day with us!"
          },
          {
            "type": "TEXT",
            "text": "We've emailed your invoice. You'll find everything you need to know there."
          }
        ]
      }
    }
  }
}
```

The above example produces this output:

| Inbox                                                     | Chat Widget                                                           |
| --------------------------------------------------------- | --------------------------------------------------------------------- |
| ![Plain message in Wix Inbox](https://s3.amazonaws.com/wixplorer-readme-images/inbox%2Fplain__inbox.png) | ![Plain message in the chat widget](https://s3.amazonaws.com/wixplorer-readme-images/inbox%2Fplain__chat-widget.png) |

## Form Messages

`FORM` messages present form data submitted by site visitors.
Form messages contain a `title`, an optional `description`,
and an array of `fields`.
Each field in the array has a `name` and submitted `value` property.

Form messages are typically sent with a direction of `VISITOR_TO_BUSINESS`.
To hide the message from the visitor, set `visibility` to `BUSINESS`.

This example contains 4 form fields and an image:

```json
{
  "direction": "VISITOR_TO_BUSINESS",
  "message": {
    "visibility": "BUSINESS",
    "payload": {
      "type": "FORM",
      "summary": "JoJo Doe made an appointment",
      "form": {
        "title": "New Spa Appointment",
        "description": "JoJo Doe made an appointment",
        "fields": [
          {
            "name": "First Name",
            "value": "JoJo"
          },
          {
            "name": "Last Name",
            "value": "Doe"
          },
          {
            "name": "Treatments",
            "value": "Massage, Mud Bath, Facial"
          },
          {
            "name": "Appointment Date",
            "value": "May 9, 2021"
          }
        ],
        "media": [
          {
            "image": {
              "url": "https://static.wixstatic.com/media/f93e3d633e79921f14330f1911fc1139.jpg/v1/fill/w_1200,h_798,al_c,q_85,usm_0.66_1.00_0.01/f93e3d633e79921f14330f1911fc1139.webp"
            }
          }
        ]
      }
    }
  }
}
```

The above example is not displayed in the visitor's chat widget because `visibility` is set to `BUSINESS`. It produces this output in Inbox:

| Inbox                                                   |
| ------------------------------------------------------- |
| ![Form message in Wix Inbox](https://s3.amazonaws.com/wixplorer-readme-images/inbox%2Fform__inbox.png) |

## Minimal Messages

`MINIMAL` messages contain a single line of text and an optional icon.
They're useful for reporting an activity that took place.
To hide the message from the visitor, set `visibility` to `BUSINESS`.

This example reports that the visitor made a spa appointment:

```json
{
  "direction": "VISITOR_TO_BUSINESS",
  "message": {
    "visibility": "BUSINESS",
    "payload": {
      "type": "MINIMAL",
      "summary": "Booked a spa appointment",
      "minimal": {
        "text": "Booked a spa appointment",
        "iconUrl": "https://static.wixstatic.com/media/727514_1a58537f1b6a44a7b09956cdbc5ac774~mv2.png/v1/fill/w_297,h_324,al_c,lg_1,q_85/727514_1a58537f1b6a44a7b09956cdbc5ac774~mv2.webp"
      }
    }
  }
}
```

The above example is not displayed in the visitor's chat widget
because `visibility` is set to `BUSINESS`.
It produces this output in Inbox:

| Inbox                                                         |
| ------------------------------------------------------------- |
| ![Minimal message in Wix Inbox](https://s3.amazonaws.com/wixplorer-readme-images/inbox%2Fminimal__inbox.png) |

## Template Messages

`TEMPLATE` messages use buttons to allow the visitor to perform actions.
Buttons can be either `ACTION` or `POSTBACK` type.
Action buttons open a specified `url` in the visitor's browser,
and postback buttons pass a `buttonPayload` to the
[Button Interacted Webhook](https://dev.wix.com/api/rest/drafts/inbox/button-interacted-webhook).

This example tells the visitor their spa appointment has been booked
and offers two buttons.
The first is an action button, and the second is a postback button:

```json
{
  "message": {
    "payload": {
      "type": "TEMPLATE",
      "summary": "JoJo, you're getting a spa day!",
      "template": {
        "title": "JoJo, you're getting a spa day!",
        "iconUrl": "https://static.wixstatic.com/media/f93e3d633e79921f14330f1911fc1139.jpg/v1/fill/w_1200,h_798,al_c,q_85,usm_0.66_1.00_0.01/f93e3d633e79921f14330f1911fc1139.webp",
        "textLines": [
          "Thanks for booking with us!",
          "You're booked for a massage, mud bath, and facial on May 9, 2021."
        ],
        "buttons": [
          {
            "label": "View My Invoice",
            "type": "ACTION",
            "url": "https://www.example.com/customer_12345/spa_day_54321/invoice.pdf"
          },
          {
            "label": "Change My Appointment",
            "type": "POSTBACK",
            "buttonPayload": {
              "appId": "ea88a721-f831-5c4b-a5ed-dddf57925aa9",
              "interactionId": "spa_day_54321__change_appointment"
            }
          }
        ]
      }
    }
  }
}
```

The above example produces this output:

| Inbox                                                           | Chat Widget                                                                 |
| --------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ![Template message in Wix Inbox](https://s3.amazonaws.com/wixplorer-readme-images/inbox%2Ftemplate__inbox.png) | ![Template message in the chat widget](https://s3.amazonaws.com/wixplorer-readme-images/inbox%2Ftemplate__chat-widget.png) |
