import uuid
from django.db import models

# Create your models here.
class Todo(models.Model):
  todo_id = models.AutoField(primary_key=True, unique=True)
  todo_desc = models.CharField(max_length=128)
  todo_complete = models.BooleanField()
  todo_delete = models.BooleanField()
  todo_index_number = models.IntegerField(default=-1)