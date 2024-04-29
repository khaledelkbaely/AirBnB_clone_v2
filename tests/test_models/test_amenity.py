#!/usr/bin/python3
"""unittest for amenity class"""
from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity


class TestAmenity(TestBasemodel):
    """represnt test cases for amenity"""

    def __init__(self, *args, **kwargs):
        """initializing class obj"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test name is string"""
        new = self.value()
        self.assertEqual(type(new.name), str)
