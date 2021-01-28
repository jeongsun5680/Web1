from django.db import models


# Create your models here.
class Story(models.Model):
    objects = models.Manager()
    story_date = models.DateField()
    story_keyword = models.CharField(max_length=255, null=True)
    story_title = models.CharField(max_length=255)
    story_content = models.TextField()
    story_image = models.ImageField(upload_to='images/', blank=True, null=True)
