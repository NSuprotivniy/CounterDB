from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from contextlib import contextmanager
import json

import requests

# Create your views here.

def index(request):
	return render(request, 'counterlike/index.html')

def get(request, post_id):
	url = 'http://localhost:9999/db/get'
	payload = {
        'post_id':post_id
    }
	r = requests.post(url, data=payload)
	JSON = r.json()
	print JSON
	likes_num = JSON['likes_num']
	context = { 
		'counter': likes_num,
		'info': JSON['info']
	}
	return HttpResponse(json.dumps(context), content_type="application/json")
			
def save(request, post_id):	
	url = 'http://localhost:9999/db/like'
	payload = {
        'post_id':post_id
    }
	r = requests.post(url, data=payload)
	JSON = r.json()
	print JSON
	likes_num = JSON['likes_num']
	context = { 
		'counter': likes_num,
		'info': JSON['info']
	}
	return HttpResponse(json.dumps(context), content_type="application/json")
