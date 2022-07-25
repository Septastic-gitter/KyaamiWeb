from django.db import models
import uuid
# Create your models here.
class Partner(models.Model):
    partner_id = models.ForeignKey('User.User', default=0, on_delete=models.CASCADE)
    partner = models.CharField(max_length=16)
    email  = models.EmailField(max_length=32)
    cell_no = models.SmallIntegerField()
    _class = models.CharField(max_length=16)
    def __str__(self):
        return self.partner

class Distributor(models.Model):
    distributor = models.CharField(max_length=16)
    email  = models.EmailField(max_length=32)
    cell_no = models.SmallIntegerField()
    distributor_id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    def __str__(self):
        return self.distributor

class Content(models.Model):
    genre = models.CharField(max_length=16)
    format = models.CharField(max_length=16)
    #item = models.ImageField()
    link = models.URLField()
    distributor = models.CharField(max_length=16)
    distributor_id= models.UUIDField()
    producer = models.IntegerField()
    producer_id= models.ForeignKey(Distributor, on_delete=models.CASCADE)
    content_id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    def __str__(self):
        return self.content_id + ' ' + self.genre

class Like(models.Model):
    reference = models.URLField()
    user = models.CharField(max_length=16)
    user_id = models.ForeignKey('User.User',default=0, on_delete=models.CASCADE)
    like_id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    def __str__(self):
        return self.like_id + ' ' + self.reference

class Upload(models.Model):
    producer = models.IntegerField()
    distributor= models.IntegerField()
    content_id= models.ForeignKey(Content, on_delete=models.CASCADE)
    upload_id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    def __str__(self):
        return self.producer