from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.IntegerField()
    isBestSelling=models.BooleanField(default=False)
    # slug=models.SlugField(null=True,db_index=True)
    def __str__ (self):
        return f"{self.title} -> ({self.rating})"
