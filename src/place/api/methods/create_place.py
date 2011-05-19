'''
Created on 2011-5-17

@author: James
'''
from django import forms
from orange.django.place import services
from orange.django.place.models import Place
from orange.django.place.utils import get_json_response
from place.api import errors, ParamConsts, ReturnConsts
from place.api.utils import get_return_dict

def cpl(request):
    cpl_form = CplForm(request.GET)
    if cpl_form.is_valid():
        place = Place()
        place.name = cpl_form.cleaned_data[ParamConsts.NAME]
        place.user_id = cpl_form.cleaned_data[ParamConsts.USERID]
        place.app_id = cpl_form.cleaned_data[ParamConsts.APPID]
        place.latitude = cpl_form.cleaned_data[ParamConsts.LATITUDE]
        place.longitude = cpl_form.cleaned_data[ParamConsts.LONGTITUDE]
        place.radius = cpl_form.cleaned_data[ParamConsts.RADIUS]
        place.post_type = cpl_form.cleaned_data[ParamConsts.POSTTYPE]

        services.new_place(place);

        returnCode = ReturnConsts.SUCCESS
        return get_json_response(get_return_dict(returnCode, {ParamConsts.PLACEID: place.id}))
    else:
        returnCode = errors.PARAM_ERROR
        return get_json_response(get_return_dict(returnCode, message=cpl_form.errors))

class CplForm(forms.Form):
    
    #appId = ParamConsts.APPID + '= forms.CharField(max_length=100)'
    #compile(appId, '', 'exec')
    #exec(appId) 
        
    fields = ParamConsts.USERID + '= forms.CharField(max_length=100)\n'    
    fields += ParamConsts.APPID + '= forms.CharField(max_length=100)\n'
    fields += ParamConsts.LONGTITUDE + '= forms.FloatField()\n'
    fields += ParamConsts.LATITUDE + '= forms.FloatField()\n'
    fields += ParamConsts.NAME + '= forms.CharField(max_length=100)\n'
    fields += ParamConsts.RADIUS + '= forms.IntegerField()\n'
    fields += ParamConsts.POSTTYPE + '= forms.IntegerField()\n'
    code = compile(fields, '', 'exec')
    exec(code)
   
    #str += '\n'+longitude
    #compile(str, '', 'exec')
    #exec(str)
    
    #latitude = ParamConsts.LATITUDE + '= forms.FloatField()'
    #compile(latitude, '', 'exec')
    #exec(latitude)
    
    #name = ParamConsts.NAME + '= forms.CharField(max_length=100)'
    #compile(name, '', 'exec')
    #exec(name)
    
    #radius = ParamConsts.RADIUS + '= forms.IntegerField()'
    #compile(radius, '', 'exec')
    #exec(radius)

    #postType = ParamConsts.POSTTYPE + '= forms.IntegerField()'
    #compile(postType, '', 'exec')
    #exec(postType)
    
    #userId = ParamConsts.USERID + '= forms.CharField(max_length=100)'    
    #compile(userId, '', 'exec')
    #exec(userId)
    
    #uid = forms.CharField(max_length=100)
    #app = forms.CharField(max_length=100)
    #lo = forms.FloatField()
    #lat = forms.FloatField()
    #na = forms.CharField(max_length=100)
    #ra = forms.IntegerField()
    #pt = forms.IntegerField()
