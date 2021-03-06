from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    text = models.TextField(max_length=50000)
    image = models.ImageField(upload_to='event_images/')

    def summary_text(self):
        return self.text[:500] + "..."

    #shows title at admin panel in 'Blog'
    def __str__(self):
        return self.title
# Create your models here.
