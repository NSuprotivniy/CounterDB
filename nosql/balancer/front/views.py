from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from contextlib import contextmanager
from django.conf import settings
import json

import requests

# Create your views here.

class Nodes:
	nodes_list = []
	size = 0

	def balance(self, post_id):
		if self.size == 1:
			return self.nodes_list[0]
		return self.nodes_list[int(post_id) % self.size]

def get_nodes():
	nodes = Nodes()
	nodes.nodes_list = []
	nodes.size = 0
	return nodes

nodes = get_nodes()
nodes.nodes_list = settings.NODES_LIST['n_list']
nodes.size = settings.NODES_LIST['n_number']


def index(request):
	return render(request, 'counterlike/index.html')

def get(request, post_id):
	url = nodes.balance(post_id)
	print url
	url = url + "db/get"
	payload = {
        'post_id':post_id
    }
	r = requests.post(url, data=payload)
	JSON = r.json()
<<<<<<< HEAD
	#print JSON
=======
	domain = request.get_host()
	print domain
	print JSON
>>>>>>> 84ee01ecda5a4810fd2902586d97c41e9e821208
	likes_num = JSON['likes_num']
	context = { 
		'counter': likes_num,
		'info': {
			'hit': JSON['info'],
			'node': url
		}
	}
	return HttpResponse(json.dumps(context), content_type="application/json")
			
def save(request, post_id):	
	url = nodes.balance(post_id)
	print url
	url = url + "db/like"
	payload = {
        'post_id':post_id
    }
	r = requests.post(url, data=payload)
	JSON = r.json()
<<<<<<< HEAD
	#print JSON
=======
	domain = request.get_host()
	print domain
	print JSON
>>>>>>> 84ee01ecda5a4810fd2902586d97c41e9e821208
	likes_num = JSON['likes_num']
	context = { 
		'counter': likes_num,
		'info': {
			'hit': JSON['info'],
			'node': url
		}
	}
	return HttpResponse(json.dumps(context), content_type="application/json")
