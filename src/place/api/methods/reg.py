'''
Created on 2011-5-16

@author: James
'''
from django import forms
from orange.django.place import services
from orange.django.place.exceptions import UserExistError
from orange.django.place.models import User
from orange.django.place.utils import get_json_response
from place.api import errors
from place.api.utils import ParamConsts, ReturnConsts, get_return_dict

def reg(request):
    reg_form = RegForm(request.GET);
    if reg_form.is_valid():
        print reg_form.changed_data
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
    lid = forms.CharField(max_length=50)
    lty = forms.IntegerField()
    did = forms.CharField(max_length=150)
    dos = forms.IntegerField()
    dm = forms.CharField(max_length=50)
    cc = forms.CharField(max_length=20, required=False)
    lang = forms.CharField(max_length=20, required=False)
    dto = forms.CharField(max_length=150, required=False)
