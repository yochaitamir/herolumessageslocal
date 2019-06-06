from django.shortcuts import render
from django.http import HttpResponse
from .models import Messages
import json
from django.db.models import Case, CharField, Value, When
from django.core import serializers
from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("Hello World")
@csrf_exempt
def write_message(request):
    if request.method == 'POST':
        try:
            message = Messages()
            sender=User.objects.get(username=request.POST.get('sender'))
            reciever=User.objects.get(username=request.POST.get('reciever'))
            message.sender= sender
            message.reciever= reciever
            message.message= request.POST.get('message')
            message.subject= request.POST.get('subject')
            message.creation_date= datetime.now()
            message.read=False
            message.save()
            return HttpResponse("message was created successfully")
        except:
            return HttpResponse("Either sender or reciever dont exist in the data-base")



@csrf_exempt
def get_all_messages(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            messages=Messages.objects.filter(reciever=user)
            qs_json = serializers.serialize('json', messages)
            for x in messages:
                x.creation_date=x.creation_date
                x.read=True
                x.save()
            return HttpResponse(qs_json, content_type='application/json') 
        else:
            return HttpResponse("no authenticated user")

    
def get_all_unread_messages(request,user):
    messages=Messages.objects.filter(reciever=user,read=False)
    qs_json = serializers.serialize('json', messages)
    for x in messages:
        x.creation_date=x.creation_date
        x.read=True
        x.save()
    return HttpResponse(qs_json, content_type='application/json')
def delete_message(request,mpk,user):
    try:
        y=Messages.objects.get(pk=mpk , sender=user)
        y.delete()
        return HttpResponse("Deleted successfully")
    except:
        pass
    try:
        x=Messages.objects.get(pk=mpk , reciever=user)
        x.delete()
        return HttpResponse("Deleted successfully")
    except:
        return HttpResponse("Cannot Delete!!!")
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            return HttpResponse(user) 
        else:
            return HttpResponse("no authenticated user")
