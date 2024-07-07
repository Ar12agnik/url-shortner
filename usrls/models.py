from django.db import models

# Create your models here.
class url_hash(models.Model):
    original_url=models.CharField(max_length=1000)
    time=models.TimeField( auto_now=False, auto_now_add=True)
    hash=models.CharField(max_length=1000)