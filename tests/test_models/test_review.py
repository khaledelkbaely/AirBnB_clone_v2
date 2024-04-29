#!/usr/bin/python3
"""unittests for Review class"""
from tests.test_models.test_base_model import TestBasemodel
from models.review import Review


class TestReview(TestBasemodel):
    """represnt unittests for Review class"""

    def __init__(self, *args, **kwargs):
        """Initialize instance"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test type of place_id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test type of user_id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test type of text"""
        new = self.value()
        self.assertEqual(type(new.text), str)
