#!/usr/bin/python3
"""Test for place class"""
from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """test place class"""

    def __init__(self, *args, **kwargs):
        """initialize instance"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test type of id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test type of user_id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test type of name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test type of description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test type of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test type of number_bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test type of max_guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test type of price_by_night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test type of latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test type of longitude"""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """test type of amenity_ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
