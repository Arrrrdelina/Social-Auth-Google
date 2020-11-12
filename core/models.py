from django.db import models


class Profile(models.Model):
    name = models.CharField('Enter your name', max_length=30)
    email = models.CharField('Enter your mail', max_length=40)

    def __str__(self):
        return self.name

