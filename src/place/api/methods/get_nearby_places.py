'''
Created on 2011-5-20

@author: James
'''
from django import forms
from orange.django.place import services
from orange.django.place.utils import get_json_response
from orange.place import errors
from place.api import ParamConsts
from place.api.utils import get_return_dict

def gnp(request):
    gnp_form = GnpForm(request.GET)
    if gnp_form.is_valid():
        latitude = gnp_form.cleaned_data[ParamConsts.LATITUDE]
        longtitude = gnp_form.cleaned_data[ParamConsts.LONGTITUDE]

        places = services.get_nearby_places(latitude, longtitude)
        returnCode = errors.ERROR_SUCCESS
        return get_json_response(get_return_dict(returnCode, __get_return_list(places)))
    else:
        returnCode = errors.ERROR_PARAMETER
        return get_json_response(get_return_dict(returnCode, message=gnp_form.errors))

def __get_return_list(places):
    result = []
    for place in places:
        place_dict = {}
        place_dict[ParamConsts.PLACEID] = place.id
        place_dict[ParamConsts.CREATE_USERID] = place.user_id
        place_dict[ParamConsts.LONGTITUDE] = place.longitude
        place_dict[ParamConsts.LATITUDE] = place.latitude
        place_dict[ParamConsts.NAME] = place.name
        place_dict[ParamConsts.DESC] = place.desc
        place_dict[ParamConsts.RADIUS] = place.radius
        place_dict[ParamConsts.POSTTYPE] = place.post_type
        result.append(place_dict)
    return result

class GnpForm(forms.Form):
    fields = ParamConsts.USERID + '= forms.CharField(max_length=100)\n'
    fields += ParamConsts.APPID + '= forms.CharField(max_length=50)\n'
    fields += ParamConsts.LATITUDE + '= forms.FloatField()\n'
    fields += ParamConsts.LONGTITUDE + '= forms.FloatField()\n'
    code = compile(fields, '', 'exec')
    exec(code)
