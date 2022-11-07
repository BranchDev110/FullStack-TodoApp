from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class RequestTodoAdmin(admin.ModelAdmin):
  list_display = ['todo_id', 'todo_desc', 'todo_complete', 'todo_delete']