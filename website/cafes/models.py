from django.db import models


# Create your models here.
class Cafes(models.Model):
    photo = models.CharField(max_length = 400)
    name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 400)
    g_rating = models.DecimalField(max_digits = 2, decimal_places = 1)
    work_conditions = models.DecimalField(max_digits = 2, decimal_places = 1)

    def __str__(self):
        return self.name
