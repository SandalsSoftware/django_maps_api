from django.test import TestCase, Client
from .google_maps_distance_calc import GoogleDistanceCalc


class TestGoogleDistanceAPI(TestCase):
    """ Test the google API. Requires internet access.
    Some errors may occur if the max daily limit for the API key
    or the IP address are hit (roughly 2000 requests per day)
    """

    def setUp(self):
        self.google = GoogleDistanceCalc()

    def test_get_coords(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        coords = (37.4225456, -122.0842498)
        actual_coords = self.google.get_coords(address)
        rounding_precision=[2,2]
        self.assertEqual(map(round, coords,rounding_precision),
            map(round, actual_coords,rounding_precision))

    def test_get_address_distance(self):
        """ test the distance between google HQ and
        california capital"""
        address1 = "1600 Amphitheatre Parkway, Mountain View, CA"
        address2 = "Sacramento, CA 95814"
        expected_result = {'distance': u'194 km',
                           'distance_meters': 194165,
                           'duration': u'2 hours 2 mins',
                           'duration_seconds': 7307
                           }
        actual_result = self.google.get_address_distance(address1, address2)
        #Google may return slightly different results over time
        # so just make sure it is in the general range
        distance_in_range = True if\
            expected_result['distance_meters']-5000 < actual_result['distance_meters'] and \
            expected_result['distance_meters']+5000 > actual_result['distance_meters'] \
            else False
        time_in_range = True if \
            expected_result['duration_seconds'] - (5*60) < actual_result['duration_seconds'] and \
            expected_result['duration_seconds'] + (5*60) > actual_result['duration_seconds'] \
            else False
        self.assertTrue(distance_in_range)
        self.assertTrue(time_in_range)

    def test_get_coords_distance(self):
        """ test the distance between google HQ and
        california capital, in coords"""
        coord1 = (37.4225456, -122.0842498)
        coord2 = (38.5824933, -121.4941738)
        expected_result = {'distance': u'194 km',
                           'distance_meters': 193985,
                           'duration': u'2 hours 2 mins',
                           'duration_seconds': 7308
                           }
        actual_result = self.google.get_coords_distance(coord1, coord2)
        #Google may return slightly different results over time
        # so just make sure it is in the general range
        distance_in_range = True if\
            expected_result['distance_meters']-5000 < actual_result['distance_meters'] and \
            expected_result['distance_meters']+5000 > actual_result['distance_meters'] \
            else False
        time_in_range = True if \
            expected_result['duration_seconds'] - (5*60) < actual_result['duration_seconds'] and \
            expected_result['duration_seconds'] + (5*60) > actual_result['duration_seconds'] \
            else False
        self.assertTrue(distance_in_range)
        self.assertTrue(time_in_range)
