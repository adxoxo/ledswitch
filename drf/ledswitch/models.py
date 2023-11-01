from django.db import models

# Create your models here.
class LedSTATE(models.Model):
    is_on = models.BooleanField(default=False)
