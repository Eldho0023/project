from django.db import models

# Create your models here.

from datetime import timedelta

class Recipes(models.Model):
    name=models.CharField(max_length=250)
    prep_time=models.DurationField(default=timedelta(minutes=120))
    diff_choices=[
        (1,'Easy'),
        (2,'Medium'),
        (3,'Hard')
    ]
    difficulty=models.IntegerField(choices=diff_choices)
    vegitarian=models.BooleanField()
    Description=models.CharField(max_length=5000)
    Recipe_img=models.ImageField(upload_to="recipe/")
