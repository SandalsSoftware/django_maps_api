"""
Implements distance_calc using the Google Maps API.

For more information on the API specifications, see:
https://developers.google.com/maps/documentation/distancematrix/
"""

import requests
import json
from .distance_calc import DistanceCalculator, MappingException


class GoogleDistanceCalc(DistanceCalculator):
    __geocode_url = "http://maps.google.com/maps/api/geocode/json"
    __matrix_url = "http://maps.googleapis.com/maps/api/distancematrix/json"
    __output_type = "json"
    __output_language = "en"
    __route_avoidance = "ferries"

    def get_coords(self, address):
        """return a (latitude, longitude) pair that corresponds to the given
        address
        """
        params = {
            "address": address,
            "key": self.API_key,
            "language": self.__output_language,
            "avoid": self.__route_avoidance,
        }
        r = requests.get(self.__geocode_url, params=params)
        data = r.json()
        if data['status'] == 'ZERO_RESULTS':
            raise MappingException("No mapping results found for address " + address)
        return (data['results'][0]['geometry']['location']['lat'], data['results'][0]['geometry']['location']['lng'])

    def get_address_distance(self, address1, address2):
        params = {
            "origins": address1,
            "destinations": address2,
            "key": self.API_key,
            "language": self.__output_language,
            "avoid": self.__route_avoidance,
        }
        r = requests.get(self.__matrix_url, params=params)
        data = r.json()
        try:
            if data['rows'][0]['elements'][0]['status'] != "OK":
                error_msg = "%s for addresses %s, %s" % (
                    data['rows'][0]['elements'][0]['status'],
                    repr(address1),
                    repr(address2),
                    )
                raise MappingException(error_msg)
        except IndexError:
            error_msg = "Error locating addresses %s, %s" % (
                    repr(address1),
                    repr(address2),
                    )
            raise MappingException(error_msg)
        distance = {
            "distance": data['rows'][0]['elements'][0]['distance']['text'],
            "distance_meters": data['rows'][0]['elements'][0]['distance']['value'],
            "duration": data['rows'][0]['elements'][0]['duration']['text'],
            "duration_seconds": data['rows'][0]['elements'][0]['duration']['value'],
        }
        return distance

    def get_coords_distance(self, coord1, coord2):
        address1 = "%s, %s" % coord1
        address2 = "%s, %s" % coord2
        return self.get_address_distance(address1, address2)
