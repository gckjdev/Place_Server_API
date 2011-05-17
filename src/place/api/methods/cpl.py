'''
Created on 2011-5-17

@author: James
'''
from django import forms
from orange.django.place import services
from orange.django.place.models import Place
from orange.django.place.utils import get_json_response
from place.api import errors
from place.api.methods.reg import get_return_dict
from place.api.utils import Constants

def cpl(request):
    cpl_form = CplForm(request.GET)
    if cpl_form.is_valid():
        place = Place()
        place.name = cpl_form.cleaned_data[Constants.PARA_NAME]
        place.user_id = cpl_form.cleaned_data[Constants.PARA_USERID]
        place.app_id = cpl_form.cleaned_data[Constants.PARA_APPID]
        place.latitude = cpl_form.cleaned_data[Constants.PARA_LATITUDE]
        place.longitude = cpl_form.cleaned_data[Constants.PARA_LONGTITUDE]
        place.radius = cpl_form.cleaned_data[Constants.PARA_RADIUS]
        place.post_type = cpl_form.cleaned_data[Constants.PARA_POSTTYPE]

        services.new_place(place);

        returnCode = Constants.RET_SUCCESS
        return get_json_response(get_return_dict(returnCode, {Constants.PARA_PLACEID: place.id}))
    else:
        returnCode = errors.PARAM_ERROR
        return get_json_response(get_return_dict(returnCode, message=cpl_form.errors))

class CplForm(forms.Form):
    uid = forms.CharField(max_length=100)
    app = forms.CharField(max_length=100)
    lo = forms.FloatField()
    lat = forms.FloatField()
    na = forms.CharField(max_length=100)
    ra = forms.IntegerField()
    pt = forms.IntegerField()