from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    creator = models.ForeignKey(User, on_delete=models)
    #on_delete = deletes objects related to it

    context = models.IntegerField()
    location = models.CharField(max_length=2 )
    created_at = models.DateTimeField(auto_now_add=True)
    #CONTENT = DATATPYE
    #ung foreign key is relationship
