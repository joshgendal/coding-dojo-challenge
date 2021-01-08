from django.db import models

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateTimeField('release date')
    network = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.title