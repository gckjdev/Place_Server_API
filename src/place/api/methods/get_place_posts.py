'''
Created on 2011-5-18

@author: James
'''
from django import forms
from orange.django.place import services
from orange.django.place.utils import get_json_response

from orange.place import errors
from place.api import ParamConsts
from place.api.utils import get_return_dict, date2str

def gpp(request):
    gpp_form = GppForm(request.GET)
    if gpp_form.is_valid():
        place_id = gpp_form.cleaned_data[ParamConsts.PLACEID]
        before = gpp_form.cleaned_data[ParamConsts.AFTER_TIMESTAMP]
        max_count = gpp_form.cleaned_data[ParamConsts.MAX_COUNT]
        posts = services.get_place_posts(place_id, before, max_count)

        returnCode = errors.ERROR_SUCCESS
        return get_json_response(get_return_dict(returnCode, __get_return_list(posts)))
    else:
        returnCode = errors.ERROR_PARAMETER
        return get_json_response(get_return_dict(returnCode, message=gpp_form.errors))

def __get_return_list(posts):
    result = []
    for post in posts:
        post_dict = {}
        post_dict[ParamConsts.POSTID] = post.id
        post_dict[ParamConsts.USERID] = post.user_id
        post_dict[ParamConsts.LATITUDE] = post.latitude
        post_dict[ParamConsts.LONGTITUDE] = post.longitude
        post_dict[ParamConsts.USER_LATITUDE] = post.user_latitude
        post_dict[ParamConsts.USER_LONGITUDE] = post.user_longitude
        post_dict[ParamConsts.TEXT_CONTENT] = post.text_content
        post_dict[ParamConsts.CONTENT_TYPE] = post.content_type
        post_dict[ParamConsts.CREATE_DATE] = date2str(post.create_time)
        result.append(post_dict)
    return result

class GppForm(forms.Form):
    
    fields = ParamConsts.USERID + '= forms.CharField(max_length=100)\n'    
    fields += ParamConsts.APPID + '= forms.CharField(max_length=50)\n'
    fields += ParamConsts.PLACEID + '= forms.CharField(max_length=100)\n'
    fields += ParamConsts.AFTER_TIMESTAMP + '= forms.CharField(max_length=100, required=False)\n'
    fields += ParamConsts.MAX_COUNT + '= forms.IntegerField()\n'
    code = compile(fields, '', 'exec')
    exec(code)
        
    #pid = forms.CharField(max_length=100)
    #at = forms.CharField(max_length=100, required=False)
    #mc = forms.IntegerField()
