from django.http import HttpResponse
from orange.place import service
from orange.place.model import Post, Place
import json

def place_list(request):
    places = service.get_place_list()
    return __get_json_response(Place, places)

def place_info(request, key):
    place = service.get_place(key)
    return __get_json_response(Place, place)

def place_posts(request, key):
    posts = service.get_place_posts(key);
    return __get_json_response(Post, posts)

def post_info(request, key):
    post = service.get_post(key)
    return __get_json_response(Post, post)

def post_replies(request, key):
    replies = service.get_post_replies(key)
    return __get_json_response(Post, replies)

def __get_json_response(cls, obj):
    return HttpResponse(__to_json(cls, obj), content_type='application/json')

def __to_json(cls, obj):
    return json.dumps(obj, default=cls.json_default)

