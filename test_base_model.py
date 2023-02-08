#!/usr/bin/env python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My first Model"
my_model.number = 89
print(my_model)
print(my_model.id)
print(type(my_model))
