import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    
    def test_init(self):
        """Tests if instance is correctly initialized"""

        model = BaseModel()
        self.assertIsInstance(model, Basemodel)
        self.assertIsInstance(model.id,str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)


    def test_save(self):
        """Tests if save method updates the updated_at attribute"""

        model = BaseModel()
        created_at = model.updated_at
        model.save()
        self.assertNotEqual(created, model.updated_at)


    def test_to_dict(self):
        """Test if to_dict method returns a dictionary containing 
        all attributes of the instance
        """

        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()

