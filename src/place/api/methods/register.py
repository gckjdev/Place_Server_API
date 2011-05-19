'''
Created on 2011-5-16

@author: James
'''
from django import forms
from orange.django.place import services
from orange.django.place.exceptions import UserExistError
from orange.django.place.models import User
from orange.django.place.utils import get_json_response
from place.api import ParamConsts, ReturnConsts, errors
from place.api.utils import get_return_dict

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

        returnCode = ReturnConsts.SUCCESS
        try:
            services.register_user(user)
        except UserExistError as e:
            returnCode = e.code 

        if returnCode == ReturnConsts.SUCCESS:
            return get_json_response(get_return_dict(returnCode, {ParamConsts.USERID: user.id}))
        else:
            return get_json_response(get_return_dict(returnCode))
    else:
        returnCode = errors.PARAM_ERROR
        return get_json_response(get_return_dict(returnCode, message=reg_form.errors))

class RegForm(forms.Form):
    #lid = forms.CharField(max_length=50)
    #lty = forms.IntegerField()
    #did = forms.CharField(max_length=150)
    #dos = forms.IntegerField()
    #dm = forms.CharField(max_length=50)
    #cc = forms.CharField(max_length=20, required=False)
    #lang = forms.CharField(max_length=20, required=False)
    #dto = forms.CharField(max_length=150, required=False)
    
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
    
    
