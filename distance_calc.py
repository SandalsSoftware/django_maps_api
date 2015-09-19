"""
Distance calc is a toolset that enables looking up the estimated driving
distance between two points or addresses. It does not return directions or
any data other than expected travel time and distance.

"""

from abc import ABCMeta, abstractmethod


class MappingException(Exception):
    pass


class DistanceCalculator:
    __metaclass__ = ABCMeta
    __API_key = ""

    def __init__(self):
        self.__API_key = ""

    @abstractmethod
    def get_coords(self, address):
        """return a (latitude, longitude) pair that corresponds to the given
         address"""
        pass

    @abstractmethod
    def get_address_distance(self, address1, address2):
        """Return the driving distance, in KM,  and the approximate drive time,
        between address1 and address2. If it is not possible to drive between
        them, return None."""
        pass

    @abstractmethod
    def get_coords_distance(self, coord1, coord2):
        """Return the driving distance, in KM, and the approximate drive time,
        between two coordinates. Coordinates should be in the standard form
        of (lat, lng), same as returned by get_coords.
            Example coordinate data:
                {u'lat': 37.4225456, u'lng': -122.0842498}
        If it is not possible to drive between them, return None.
        """
        pass

    @property
    def API_key(self):
        return self.__API_key

    @API_key.setter
    def API_key(self, key):
        self.__API_key = key
