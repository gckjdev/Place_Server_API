'''
Created on 2011-5-20

@author: James
'''
from django import forms
from django.views.decorators.cache import never_cache
from orange.django.place import services
from orange.django.place.utils import get_json_response
from orange.place import errors
from place.api import ParamConsts
from place.api.utils import get_return_dict

@never_cache
def ufp(request):
    ufp_form = UfpForm(request.GET)
    if ufp_form.is_valid():
        user_id = ufp_form.cleaned_data[ParamConsts.USERID]
        place_id = ufp_form.cleaned_data[ParamConsts.PLACEID]
        services.user_follow_place(user_id, place_id);
        return_code = errors.ERROR_SUCCESS
        return get_json_response(get_return_dict(return_code))
    else:
        returnCode = errors.ERROR_PARAMETER
        return get_json_response(get_return_dict(returnCode, message=ufp_form.errors))
    pass

class UfpForm(forms.Form):
    fields = ParamConsts.USERID + '= forms.CharField(max_length=100)\n'
    fields += ParamConsts.APPID + '= forms.CharField(max_length=50)\n'
    fields += ParamConsts.PLACEID + '= forms.CharField(max_length=100)\n'
    code = compile(fields, '', 'exec')
    exec(code)

