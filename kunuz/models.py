from django.db import models
from django.contrib.auth.models import User

class New(models.Model):
    theme = models.CharField(max_length=300,null=True)
    text = models.CharField(max_length=1000,null=True)
    tag = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except Exception as e:
            print('Error')
            return ''
    def __str__(self):
        return self.theme