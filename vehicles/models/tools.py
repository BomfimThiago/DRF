from django.db import models

# Create your models here.
class Tool:
    def __init__(self, name, make):
        self.name = name
        self.make = make
