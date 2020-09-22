from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Message(UserModel):
    message = models.CharField(max_length=300)
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.message
