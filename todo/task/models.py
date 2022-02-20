from turtle import title
from django.db import models
from django.forms import CharField

# Create your models here
# class name - table; the variables - columns of the table
# no need to work with SQL to interact with database, we can interact through models
# migrations made when models are added; or something added to database

class task(models.Model):
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    createdDate=models.DateTimeField(auto_created=True)


    # function defined in the class
    def __str__(self): 
        return self