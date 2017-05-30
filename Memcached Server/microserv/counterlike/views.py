from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from contextlib import contextmanager
import json
import pylibmc

import datetime, re

from .models import Post

# Create your views here.


mc_addrs = "127.0.0.1"
mc_pool_size = 16


class ClientPool(list):
    @contextmanager
    def reserve(self):
        mc = self.pop()
        try:
            yield mc
        finally:
            self.append(mc)


mc = pylibmc.Client(mc_addrs)
mc_pool = ClientPool(mc.clone() for i in range(mc_pool_size))


class LikesView():

	def index (request):
		return render(request, 'counterlike/index.html')

	def get (request, post_id):
		with mc_pool.reserve() as mc:
			likes_cnt = mc.get(post_id)
			context = { 'post_id': post_id, 'counter': likes_cnt }
			#return render(request, 'counterlike/index.html', context)
			return HttpResponse(json.dumps(context), content_type="application/json")
			
	def save(request, post_id):	
		with mc_pool.reserve() as mc:	
			try:
				mc.incr(str(post_id))
			except pylibmc.NotFound:
				mc.set(str(post_id), 1)
			
			likes_cnt = mc.get(post_id)
			context = { 'post_id': post_id, 'counter': likes_cnt }
			#return render(request, 'counterlike/index.html', context)
			return HttpResponse(json.dumps(context), content_type="application/json")
