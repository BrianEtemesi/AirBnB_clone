#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

user1 = User()

print(user1.__dict__)
