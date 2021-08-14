from django.db import models

# Create your models here.

class Article (models.Model):
    title = models.CharField(max_length = 64)
    slug = models.SlugField()
    blody = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # in add thumbnail
    # add to outhor
    def __str__(self):
        return self.title
    
    def snippet (self):
        return self.blody[0:50] + "..."

