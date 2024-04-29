#!/usr/bin/python3
"""Module for unittesting State class"""
from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class TestState(TestBasemodel):
    """represnt test State class"""

    def __init__(self, *args, **kwargs):
        """Initialize instance"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test type of name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
