SortOrder: 0
# About the Waitlist API

Use the Waitlist API to enable interested clients to sign up to be notified when a spot opens up in a fully-booked session or service. 
The service adds the client to the waitlist, notifies them when a spot has become available and reserves the spot for a set amount of time, during which they can book the spot.
>**Important**:  
Use of the waitlist functionality is currently limited to sessions with type = EVENT.

The service will suggest the opened spot to waitlised clients in the order of registration to the waitlist (first-come, first-served). 

Upon reaching the end of the list, with no one accepting the invitation to join the session, the spot becomes opened to everyone (anyone can book that spot, even if they are not waitlist participants). The next time a spot opens up, the service start over again from the top of the waitlist.

## Terminology

- **Waitlist**: A list of participants that requested to be added to a session that is fully booked, if there should be a cancellation.
- **Suggesting**: When a spot opens up in a session with a waitlist, the session is locked for bookings from any participant, other than the participant that is currently in queue in the waitlist - so that only the "suggested" participant is able to book the session.
- **Waitlist Time Window**: How much time a client has to book a place in the session, before it is offered to the next client on the waitlist.

## Use Cases

### Book a visitor to the waitlist and then to the session
![image](https://s3.amazonaws.com/wixplorer-readme-images/bookings---waitlist-service/BookToWaitlist.png)
