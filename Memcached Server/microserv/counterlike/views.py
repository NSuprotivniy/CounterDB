from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from contextlib import contextmanager
import json

import requests

# Create your views here.

def index(request):
	return render(request, 'counterlike/index.html')

def get(request, post_id):
	url = 'http://localhost:9000/node/get'
	payload = {
        'post_id':post_id
    }
	r = requests.post(url, data=payload)
    # r should return JSON
    # TODO parse JSON
	JSON = r.json()
	context = { 'post_id': JSON['likes_num'] }
	#return render(request, 'counterlike/index.html', context)
	return HttpResponse(json.dumps(context), content_type="application/json")
			
def save(request, post_id):	
	url = 'http://localhost:9000/node/like'
	payload = {
        'post_id':post_id
    }
	r = requests.post(url, data=payload)
    # r should return JSON
    # TODO parse JSON
	JSON = r.json()
	context = { 'post_id': JSON['likes_num'] }
	#return render(request, 'counterlike/index.html', context)
	return HttpResponse(json.dumps(context), content_type="application/json")
