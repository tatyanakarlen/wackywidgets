from django.db import models
from django.urls import reverse

# Create your models here.
class Widget(models.Model):
  description = models.CharField(max_length=100)
  quantity = models.IntegerField()

  def get_absolute_url(self):
        return reverse('wackywidgets', kwargs={'widget_id': self.id})

  def __str__(self):
        return self.description


  