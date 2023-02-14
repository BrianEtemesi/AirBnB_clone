import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test class for BaseModel class
    """

    def setUp(self):
        """
        Set up method to run before each test case
        """
        self.model = BaseModel()
        self.model.name = "Holberton"
        self.model.my_number = 89
        self.model.created_at = datetime.datetime(2022, 3, 22, 1, 0, 0, 0)
        self.model.updated_at = datetime.datetime(2022, 3, 22, 1, 0, 0, 0)

    def tearDown(self):
        """
        Tear down method that runs after each test case
        """
        del self.model

    def test_attribute_types(self):
        """
        Test to check if attributes are correctly set and of correct type
        """
        self.assertIsInstance(self.model.name, str)
        self.assertIsInstance(self.model.my_number, int)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save_method(self):
        """
        Test to check if save method updates the `updated_at` attribute
        """
        original_update_time = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_update_time, self.model.updated_at)

    def test_str_method(self):
        """
        Test to check if the str method returns the expected output
        """
        expected_output = "[BaseModel] ({}) {}".format(self.model.id,
                                                      self.model.__dict__)
        self.assertEqual(str(self.model), expected_output)

