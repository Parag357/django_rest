# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from myapp.models import Book

# Create your views here.

@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        book = Book(name=name)
        try:
            book.save()
            response = json.dumps({ 'Message': 'Created Successfully'})
        except:
            response = json.dumps([{ 'Error': 'Creation Failed'}])

    return HttpResponse(response, content_type='application/json')

def get(request):
    if request.method == 'GET':
    	res=[]
        try:
            books = Book.objects.all()
            for book in books:
            	res.append(book.name)
            response = json.dumps(res)
        except:
            response = json.dumps({ 'Error': 'Not Found'})

    return HttpResponse(response, content_type='application/json')
