from django.db import models
# Create your models here.
# here class is used to create table 
class MyPost(models.Model):
    message= models.TextField()

    def __str__(self):
        return self.message[:20]
