from django.db import models

class Integral(models.Model):
    type_method =models.CharField(max_length=200)
    expression =models.CharField(max_length=200)
    sub_intervals = models.IntegerField(default=0)
    result = models.FloatField(default=0)

