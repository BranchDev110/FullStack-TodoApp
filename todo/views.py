import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.core import serializers
from .serializers import TodoSerializer
from django.db.models import Max
from .models import Todo

# Create your views here.

def translateTodoObjectToJson(item):
    return {"todo_id": item.todo_id, "todo_desc": item.todo_desc, "todo_complete": item.todo_complete, "todo_delete": item.todo_delete, "todo_index_number": item.todo_index_number}

class TodoView(APIView):
    def post(self, request):
        max_index = Todo.objects.aggregate(Max('todo_index_number'))
        index = 0
        if not max_index["todo_index_number__max"] is None:
            index = max_index["todo_index_number__max"]
        index += 1024
        todo = Todo(todo_desc = request.data.get('todo_desc'), todo_complete = False, todo_delete = False, todo_index_number=index)
        todo.save()
        return JsonResponse(translateTodoObjectToJson(todo))

    def get(self, request):
        mydata = Todo.objects.all().order_by('todo_index_number').values()
        obj_list = []
        for item in mydata:
            if item['todo_delete'] is False:
                obj_list.append(item)
        return JsonResponse({"todo": obj_list}, status=200)

class TodoUpdateView(APIView):
    def post(self, request):
        updated_item = Todo.objects.get(todo_id=request.data.get('id'))
        updated_item.todo_complete = not updated_item.todo_complete
        updated_item.save()
        return JsonResponse(translateTodoObjectToJson(updated_item))


class TodoDeleteView(APIView):
    def post(self, request):
        deleted_item = Todo.objects.get(todo_id=request.data.get('id'))
        deleted_item.todo_delete = True
        deleted_item.save()
        return JsonResponse(translateTodoObjectToJson(deleted_item))


class TodoClearView(APIView):
    def post(self, request):
        obj_list = []
        for item in Todo.objects.all():
            if item.todo_complete is True:
                item.todo_delete = True
                item.save()
                obj_list.append(translateTodoObjectToJson(item))
        return JsonResponse({"todo": obj_list}, status=200)


class TodoChangeView(APIView):
    def post(self, request):
        src = Todo.objects.get(todo_id = request.data.get('src'))
        
        destf = request.data.get('destf')
        destn = request.data.get('destn')

        destf_index = 0
        if not destf is -1:
            destf_index = Todo.objects.get(todo_id = request.data.get('destf')).todo_index_number
        
        destn_index = Todo.objects.aggregate(Max('todo_index_number'))["todo_index_number__max"] + 1024
        if not destn is -1:
            destn_index = Todo.objects.get(todo_id = request.data.get('destn')).todo_index_number

        src.todo_index_number = (destf_index + destn_index) / 2
        src.save()
        return Response("Hello")