from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User,AbstractUser
from messages import settings

class Messages(models.Model):
    sender= models.ForeignKey(User, db_column="sender",to_field='username',on_delete=models.CASCADE)
    reciever=models.ForeignKey(User,related_name="rec",to_field='username', db_column="reciever",on_delete=models.CASCADE)
    message=models.CharField ( max_length=200, null=True, blank=True) 
    subject=models.CharField ( max_length=200, null=True, blank=True)
    creation_date=models.DateTimeField(default=datetime.now)
    read=models.BooleanField(("read"))
    
    