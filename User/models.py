from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    username = models.CharField(max_length=16, unique=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    role = models.CharField(max_length=16)
    email = models.EmailField(max_length=32)
    blocked = models.BooleanField(default=False)
    def __str__(self):
        return self.username

#class Artist(models.Model):
#    artist_id = models.ForeignKey(User, on_delete=models.CASCADE)
