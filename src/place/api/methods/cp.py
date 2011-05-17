'''
Created on 2011-5-17

@author: James
'''
from django import forms
from orange.django.place import services
from orange.django.place.models import Post
from orange.django.place.utils import get_json_response
from place.api import errors
from place.api.methods.reg import get_return_dict
from place.api.utils import Constants

def cp(request):
    cp_form = CpForm(request.GET)
    if cp_form.is_valid():
        post = Post()
        post.user_id = cp_form.cleaned_data[Constants.PARA_USERID]
        post.app_id = cp_form.cleaned_data[Constants.PARA_APPID]
        post.place_id = cp_form.cleaned_data[Constants.PARA_PLACEID]
        post.content_type = cp_form.cleaned_data[Constants.PARA_CONTENT_TYPE]
        post.text_content = cp_form.cleaned_data[Constants.PARA_TEXT_CONTENT]
        post.latitude = cp_form.cleaned_data[Constants.PARA_LATITUDE]
        post.longitude = cp_form.cleaned_data[Constants.PARA_LONGTITUDE]
        post.user_latitude = cp_form.cleaned_data[Constants.PARA_USER_LATITUDE]
        post.user_longitude = cp_form.cleaned_data[Constants.PARA_USER_LONGITUDE]

        services.new_post(post);

        returnCode = Constants.RET_SUCCESS
        return get_json_response(get_return_dict(returnCode, {Constants.PARA_PLACEID: post.id, Constants.PARA_CREATE_DATE: post.create_time}))
    else:
        returnCode = errors.PARAM_ERROR
        return get_json_response(get_return_dict(returnCode, message=cp_form.errors))

class CpForm(forms.Form):
    uid = forms.CharField(max_length=100)
    app = forms.CharField(max_length=50)
    pid = forms.CharField(max_length=100)
    ct = forms.IntegerField()
    t = forms.CharField(max_length=200)
    lat = forms.FloatField()
    lo = forms.FloatField()
    ula = forms.FloatField()
    ulo = forms.FloatField()
