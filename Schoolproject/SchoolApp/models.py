from django.db import models
import os

class MyObject(models.Model):
    name=models.CharField(Max_length=100)
    email=models.CharField()

    image_url = models.CharField()

    def image_url(self):
        if os.path.exists(self.image_url):

            return self.image_url
        return 'default_image'