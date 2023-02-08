SortOrder: 0
# Conferencing Service Overview

The conferencing service allows creating conferencing meetings in a an external conferencing meetings provider system (such as Zoom).

A typical flow of using this service is as follows:

## Pre-requisites
* A conferencing provider application needs to be installed on the meta-site for which the conference meeting is to be created.

## Supported Providers
* [Zoom](https://www.wix.com/market/web-solution/zoom)

## Configuration 
* Call ConferencingService.ListProviders to get the list of supported providers
* Invoke the provider's oauth to start the process of authenticating a provider's user account
  by calling: /_api/bookings-online-meeting/v1/{providerId}/connect

## Usage 
* Call the ConferencingService.CreateConference to create a conferencing meeting based of the specific parameters of the request 
* Internally use the Conference.host_url and Conference.guest_url to expose the conference meeting in your product. 
