from django.db import models


class Event(models.Model):
    event_image = models.ImageField(upload_to='event_images/')
    event_text = models.CharField(max_length=290)

    # shows text at admin panel in 'Event'
    def __str__(self):
        return self.event_text

# Create your models here.
