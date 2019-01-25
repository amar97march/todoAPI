from django.db import models
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    owner = models.CharField(max_length=20,blank=False)
    user_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30,blank=False,unique = True)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def json(self):
        ret = {}
        ret['owner'] = self.owner
        ret['title'] = self.title
        ret['description'] = self.description
        ret['completed'] = self.completed
        ret['created'] = self.created
        return ret 