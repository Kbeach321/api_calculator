########## Imports #######################
from django.db import models
from django.contrib.auth.models import AbstractUser

################# Classes #################

class User(AbstractUser):
    pass

class Operation(models.Model):
    operand_one = models.IntegerField()
    operand_two = models.IntegerField()
    operator = models.CharField(max_length = 1)
    result = models.IntegerField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
###### FK ############
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
