SortOrder: 0
# About the Bookings v2 API

Use this API to manage bookings for a site's services.

A booking is an entity that represents a session that was ordered (but not necessarily paid for) for a specific time and rate, for a specific customer. A
customer can book a single class or an appointment (a session), or book a course, a set of sessions at once (a schedule).

A [booking](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/booking-object) contains the following information:

- **Customer information**: Contact details, including contact ID, name, email, address, phone number, amd timezone.
- **Booked entity details**: The slot or schedule that was booked, including start & end date, location, and resource.
- **Payment details**: Payment status, and the payment option the customer chose when booking. For example, online payment, in-person payment, or  membership.
- **Status**: Current booking status, including CREATED, PENDING_ECOM_CHECKOUT, CONFIRMED, CANCELED, PENDING, DECLINED, WAITING_LIST.

## Terminology

- **Visitor**: Anyone who is not registered as a member and does not login to the Wix site (upon booking, visitors are added as contacts).
- **Member**: Someone who is registered as a member in the Wix site and has a login.
- **Owner**: The Wix site owner.
- **Slot**: An available period of time in a schedule that can be booked by a customer. While this includes existing sessions that are available for booking, it
  can also represent a period of time that can be booked based on the availability of a resource. For example, a doctor with appointments of 30 minutes each that are
  open for booking every weekday between 8:00 - 17:00. These slots are calculated by the constraints defined in the schedule.
- **[Wix Paid Plans](https://support.wix.com/en/article/about-pricing-plans)**: A pre-paid bundle of services or membership including access to certain
  services.



