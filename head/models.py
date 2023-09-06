from django.db import models
from django.contrib.auth.models import User


class SliderImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"Image #{self.pk}"
