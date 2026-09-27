from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    published = models.DateTimeField(db_default=timezone.now)   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   


    class Meta:
        ordering = ('-published')
        indexes = [
            models.Index(filds =['-published']),
        ]    
    def __str__(self):
        return self.title