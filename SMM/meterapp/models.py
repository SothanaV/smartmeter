from django.db import models
from django.utils import timezone
# Create your models here.
class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class Pressure(models.Model):
	Pressure = models.FloatField(default=0.0)
	time = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ['time']
		