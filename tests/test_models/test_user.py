#!/usr/bin/python3
"""Module for unittesting User class"""
from tests.test_models.test_base_model import TestBasemodel
from models.user import User


class TestUser(TestBasemodel):
    """represnt test User class"""

    def __init__(self, *args, **kwargs):
        """Initialize instance"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test type of first_name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test type of last_name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test type of email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test type of password"""
        new = self.value()
        self.assertEqual(type(new.password), str)
