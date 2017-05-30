from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from cassandra.cqlengine.query import DoesNotExist
from contextlib import contextmanager
import pylibmc
from .models import LikeModel
# Create your views here.


def index(request):
	template = loader.get_template('cassandra_DB/index.html')
	context = {
        'likes_num': "",
    }
	return HttpResponse(template.render(context, request))

@csrf_exempt
def like(request):
    if request.POST:
        mc = pylibmc.Client(['127.0.0.1'], binary=True, behaviors={'tcp_nodelay':True,'ketama':True})
        JSON = {
            'likes_num': "no likes",
            'info': "cache hit"
        }
        req_post_id = request.POST.get("post_id", "")
        try:
            mc.incr(req_post_id)
        except pylibmc.NotFound:
            try:
                like_obj = LikeModel.objects().get(post_id = req_post_id)
            except DoesNotExist:
                insert = LikeModel(post_id = req_post_id, count_like = 1)
                insert.save()
                mc.set(req_post_id, 1)
                JSON['likes_num'] = 1
                JSON['info'] = "cache miss DB miss"
                return JsonResponse(JSON)
            like_obj.count_like = like_obj.count_like + 1
            likes_num = like_obj.count_like
            like_obj.save()
            mc.set(req_post_id, likes_num)
            JSON['likes_num'] = likes_num
            JSON['info'] = "cache miss DB hit"
            return JsonResponse(JSON)
        like_obj = LikeModel.objects().get(post_id = req_post_id)
        like_obj.count_like = like_obj.count_like + 1
        likes_num = like_obj.count_like
        like_obj.save()
        JSON['likes_num'] = likes_num
        return JsonResponse(JSON)
    return HttpResponse("not post")

@csrf_exempt
def get(request):
    if request.POST:
        mc = pylibmc.Client(['127.0.0.1'], binary=True, behaviors={'tcp_nodelay':True,'ketama':True})
        JSON = {
            'likes_num': "no likes",
            'info': "cache hit"
        }
        req_post_id = request.POST.get("post_id", "")
        likes_num = mc.get(req_post_id)
        if likes_num == None:
            try:
                like_obj = LikeModel.objects().get(post_id = req_post_id)
            except DoesNotExist:
                JSON['info'] = "cache miss DB miss"
                return JsonResponse(JSON)
            likes_num_cassandra = like_obj.count_like
            JSON['info'] = "cache miss DB hit"
            JSON['likes_num'] = likes_num_cassandra
            mc.set(req_post_id, likes_num_cassandra)
            return JsonResponse(JSON)
        else:
            JSON['likes_num'] = likes_num
            return JsonResponse(JSON)
    return HttpResponse("not post")
