from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Importance(models.Model):
    importance = models.CharField(max_length=255)

    def __str__(self):
        return self.importance


class Status(models.Model):
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    importance = models.ForeignKey(Importance, on_delete=models.CASCADE)

    def __str__(self):
        return self.todo