'''
Created on 2011-5-16

@author: James
'''
from django import forms
from django.views.decorators.cache import never_cache
from orange.django.place import services
from orange.django.place.models import User
from orange.django.place.utils import get_json_response
from orange.place import errors
from place.api import ParamConsts
from place.api.utils import get_return_dict
import logging
  

logger = logging.getLogger(__name__)

@never_cache
def reg(request):
    reg_form = RegForm(request.GET);
    if reg_form.is_valid():
        user = User()
        user.login_id = reg_form.cleaned_data[ParamConsts.LOGINID]
        user.login_id_type = reg_form.cleaned_data[ParamConsts.LOGINIDTYPE]
        user.device_id = reg_form.cleaned_data[ParamConsts.DEVICEID]
        user.device_model = reg_form.cleaned_data[ParamConsts.DEVICEMODEL]
        user.device_os = reg_form.cleaned_data[ParamConsts.DEVICEOS]
        user.device_token = reg_form.cleaned_data[ParamConsts.DEVICETOKEN]
        user.country_code = reg_form.cleaned_data[ParamConsts.COUNTRYCODE]
        user.language = reg_form.cleaned_data[ParamConsts.LANGUAGE]

        returnCode = errors.ERROR_SUCCESS
        try:
            services.register_user(user)
        except errors.ErrorException as e:
            returnCode = e.code 

        if returnCode == errors.ERROR_SUCCESS:
            return get_json_response(get_return_dict(returnCode, {ParamConsts.USERID: user.id}))
        else:
            return get_json_response(get_return_dict(returnCode))
    else:
        returnCode = errors.ERROR_PARAMETER
        return get_json_response(get_return_dict(returnCode, message=reg_form.errors))

class RegForm(forms.Form):
    
    fields = ParamConsts.LOGINID + '= forms.CharField(max_length=50)\n'    
    fields += ParamConsts.LOGINIDTYPE + '= forms.IntegerField()\n'
    fields += ParamConsts.DEVICEID + '= forms.CharField(max_length=150)\n'
    fields += ParamConsts.DEVICEOS + '= forms.IntegerField()\n'
    fields += ParamConsts.DEVICEMODEL + '= forms.CharField(max_length=200)\n'
    fields += ParamConsts.COUNTRYCODE + '= forms.CharField(max_length=20, required=False)\n'
    fields += ParamConsts.LANGUAGE + '= forms.CharField(max_length=20, required=False)\n'
    fields += ParamConsts.DEVICETOKEN + '= forms.CharField(max_length=150, required=False)\n'    
    code = compile(fields, '', 'exec')
    exec(code)
    
    
