from django.db import models

# Create your models here.

class Html(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    code = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
class Css(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    code = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
class JavaScript(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    code = models.TextField(max_length=10000)

    def __str__(self):
        return self.title

class Favourites(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    code = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
