#!/usr/bin/python3
"""unittest for city class"""
from tests.test_models.test_base_model import TestBasemodel
from models.city import City


class TestCity(TestBasemodel):
    """represent test for City class"""

    def __init__(self, *args, **kwargs):
        """initialize instance"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test the type of state_id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test type of name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
