from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    text = models.TextField(max_length=50000)
    image = models.ImageField(upload_to='event_images/')

    def summary_text(self):
        return self.text[:500] + "..."
# Create your models here.
