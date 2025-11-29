from django.db import models

# Create your models here.
class ReviewTable(models.Model):
    username = models.CharField(max_length=100)
    review_text = models.CharField(max_length=1000)
    rating = models.IntegerField()
    
    def __str__(self):
        return f"{self.username} {self.rating}"