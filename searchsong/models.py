from django.db import models

# Create your models here.

class SearchBar(models.Model):
    search = models.CharField(max_length = 250)

    def __str__(self):
        return self.search     