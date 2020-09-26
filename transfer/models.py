from django.db import models

# Employees table to contain all the employye information.

class Employees(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200) 
    duration = models.CharField(max_length=200)
    def __str__(self):
        return self.name

