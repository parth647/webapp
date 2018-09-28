from django.db import models

class Post(models.Model):
    #id is created by django by default
    title = models.CharField(max_length=140)
    body = models.TextField()
    date =  models.DateTimeField()

    def __str__(self):
        return self.title
