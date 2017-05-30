from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404

import datetime, re

from .models import Post

# Create your views here.

def index (request):
	post_list = Post.objects.order_by('-pub_date')
	context = { 'post_list': post_list}
	return render(request, 'counterlike/index.html',context)
	
def save(request, post_id):		
		post = get_object_or_404(Post, pk=post_id)
		post.count_like=post.count_like+1
		post.save()
		return HttpResponseRedirect(reverse('Likes:index'))
