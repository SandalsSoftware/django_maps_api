# Django Maps API Integration
A Django focused API integration to mapping services for Django projects.

This app is designed to allow simple integration into services like Google Maps 
for the purposes of calulating distance between two points in the world. It should 
not be used for driving directions at this time.

The most common usage is for trip optimization work, where resources are 
scattered around a geographic area, and you must send a resource to a target
location. This module can help generate the data for finding the optimal
resource to route.

Initially designed to allow the user to select google, mapquest, or other services,
currently only Google is implemented.

##Examples
Once you have checked this out into your project, you can initialize the mapping object

```python
> from maps_api.distance_calc import DistanceCalculator, MappingException
> from maps_api.google_maps_distance_calc import GoogleDistanceCalc
> 
> google = GoogleDistanceCalc()
> #set API key (optional - not setting this will limit your requests based on IP in google)
> google.API_key = "my_api_key"
> address1 = "1600 Amphitheatre Parkway, Mountain View, CA"
> address2 = "Sacramento, CA 95814"
> 
> google.get_address_distance(address1, address2)
{'distance': u'194 km',
 'distance_meters': 193978,
 'duration': u'2 hours 3 mins',
 'duration_seconds': 7370}
> google.get_coords(address1)
(37.422245, -122.0840084)
```