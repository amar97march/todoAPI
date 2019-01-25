from django.shortcuts import render
from .models import Task
import json
from rest_framework.views import APIView
from django.http import HttpResponse
from django.core.exceptions import MultipleObjectsReturned
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

class todoList(APIView):

    def post(self,request):
        
        params = json.loads(request.body)
        
        title = [i.json() for i in Task.objects.filter(title = params['title'])]
        if not title:
            title = Task(owner = params['owner'],title=params['title'],description = params['description'],completed=params['completed']).save()
            return HttpResponse('Task created')
        else:
            return HttpResponse('already exist')


    def get(self,request):
        params = json.loads(request.body)
        todo = [i.json() for i in Task.objects.filter(title = params['title'])]
        ret = {}
        ret['title']=todo
        return httpResponse(ret)

    def put(self, request):
        params = json.loads(request.body)
        ret = {}
        try:
            title = Task.objects.get(title = params['title'])
        except :
            ret['error'] = "Can't found"
            return httpResponse(ret)
        title.description = params['description']
        title.save()
        return HttpResponse('Description changed')

    def delete(self, request):
        params = json.loads(request.body)
        try:
            Task.objects.get(title=params['title']).delete()
        except:
            return HttpResponse('task not present')
        return HttpResponse('Task Deleted')

class todoListComplete(APIView):
    def put(self, request):
        params = json.loads(request.body)
        ret = {}
        try:
            title = Task.objects.filter(title = params['title']).first()
        except :
            ret['error'] = "Can't found"
            return httpResponse(ret)
        if title.completed == False:
            print('now')
            title.completed = True
        else:
            title.completed = False
        title.save()
        return HttpResponse('Toggled changed')

    
def httpResponse(data, status = True, status_code = 200):
    ret = {}
    ret['status'] =status
    ret['status_code'] = status_code
    ret['data']=data
    return HttpResponse(json.dumps(ret,sort_keys=True,cls=DjangoJSONEncoder),status=status_code,content_type="aplication/json")

