from django.db import models
from uuid import uuid4

# Create your models here.


class Books(models.Model):
  id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  titulo = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  release_yaer = models.IntegerField()
  
