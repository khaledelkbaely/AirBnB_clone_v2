#!/usr/bin/python3
"""Test Module for base class"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class TestBasemodel(unittest.TestCase):
    """test_basemodel class"""

    def __init__(self, *args, **kwargs):
        """initiatiating instance"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """set up obj before running"""
        pass

    def tearDown(self):
        """runs after finishing all tests"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """test default method"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """test to_dict method"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test kwargs with int"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            _ = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test str"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test to_dict"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """tests kwargs with None values"""
        n = {None: None}
        with self.assertRaises(TypeError):
            _ = self.value(**n)

    def test_kwargs_one(self):
        """tests kwargs with one key-value"""
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertTrue(hasattr(new, 'Name'))

    def test_id(self):
        """tests id is string"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """tests created_at and update_at are datetime instances"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
