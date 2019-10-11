from django.db import models
import os

class MyObject(models.Model):

    image_url = models.CharField()

    def image_url(self):
        if os.path.exists(self.image_url):

            return self.image_url
        return 'default_image'