'''
Created on 2011-5-17

@author: James
'''
from django import forms
from orange.django.place import services
from orange.django.place.models import Post
from orange.django.place.utils import get_json_response

from orange.place import errors
from place.api import ParamConsts
from place.api.utils import date2str, get_return_dict
import logging

logger = logging.getLogger(__name__)

def cp(request):
    cp_form = CpForm(request.GET)
    if cp_form.is_valid():
        post = Post()
        post.user_id = cp_form.cleaned_data[ParamConsts.USERID]
        post.app_id = cp_form.cleaned_data[ParamConsts.APPID]
        post.place_id = cp_form.cleaned_data[ParamConsts.PLACEID]
        post.content_type = cp_form.cleaned_data[ParamConsts.CONTENT_TYPE]
        post.text_content = cp_form.cleaned_data[ParamConsts.TEXT_CONTENT]
        post.latitude = cp_form.cleaned_data[ParamConsts.LATITUDE]
        post.longitude = cp_form.cleaned_data[ParamConsts.LONGTITUDE]
        post.user_latitude = cp_form.cleaned_data[ParamConsts.USER_LATITUDE]
        post.user_longitude = cp_form.cleaned_data[ParamConsts.USER_LONGITUDE]

        services.new_post(post);

        returnCode = errors.ERROR_SUCCESS
        return get_json_response(get_return_dict(returnCode, {ParamConsts.POSTID: post.id, ParamConsts.CREATE_DATE: date2str(post.create_date)}))
    else:
        returnCode = errors.ERROR_PARAMETER
        return get_json_response(get_return_dict(returnCode, message=cp_form.errors))

class CpForm(forms.Form):

    fields = ParamConsts.USERID + '= forms.CharField(max_length=100)\n'    
    fields += ParamConsts.APPID + '= forms.CharField(max_length=50)\n'
    fields += ParamConsts.PLACEID + '= forms.CharField(max_length=100)\n'
    fields += ParamConsts.CONTENT_TYPE + '= forms.IntegerField()\n'
    fields += ParamConsts.TEXT_CONTENT + '= forms.CharField(max_length=200)\n'
    fields += ParamConsts.LATITUDE + '= forms.FloatField()\n'
    fields += ParamConsts.LONGTITUDE + '= forms.FloatField()\n'
    fields += ParamConsts.USER_LONGITUDE + '= forms.FloatField()\n'
    fields += ParamConsts.USER_LATITUDE + '= forms.FloatField()\n'
    code = compile(fields, '', 'exec')
    exec(code)

