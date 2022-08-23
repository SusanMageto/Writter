from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    is_client = models.BooleanField('Is Client',default=False)
    is_writter = models.BooleanField('Is Writter',default=False)
    is_verified = models.BooleanField('Is Verified',default=False)





# Title
# decription
# File
# Client_amount
# Admin_amount
# due date
# status


class Task(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100,default='',null=True,blank=True)
    description = models.TextField(default='',null=True,blank=True)
    file = models.FileField(upload_to='files/',default='',null=True,blank=True)
    client_amount = models.IntegerField(default=0,null=True,blank=True)
    admin_amount = models.IntegerField(default=0,   null=True,blank=True)
    due_date = models.DateField(default='',null=True,blank=True)
    status = models.CharField(max_length=100,default='',null=True,blank=True)

    def __str__(self):
        return self.title
    
