from django.db import models
from django.utils import timezone
from django.urls import reverse

class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry-list')
    class Meta:
        verbose_name_plural = "Entries"