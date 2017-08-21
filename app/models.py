from django.db import models

class profile(models.Model):
    name = models.CharField(max_length=120)
    descriptions = models.TextField(default="my description default")
    # location = models.CharField(max_length=120, default="my location default", blank=True, null=True)
    # job = models.CharField(max_length=120, null=True)

 #   def __str__(self):
   #     return self.name