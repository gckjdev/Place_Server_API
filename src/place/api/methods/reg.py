'''
Created on 2011-5-16

@author: James
'''
from django import forms
from django.http import HttpResponse
from orange.django.place import services
from orange.django.place.models import User
from place.api.utils import Constants

def reg(request):
    regForm = RegForm(request.GET);
    if regForm.is_valid():
        print regForm.changed_data
        user = User()
        user.login_id = regForm.cleaned_data[Constants.PARA_LOGINID]
        user.login_id_type = regForm.cleaned_data[Constants.PARA_LOGINIDTYPE]
        user.device_id = regForm.cleaned_data[Constants.PARA_DEVICEID]
        user.device_model = regForm.cleaned_data[Constants.PARA_DEVICEMODEL]
        user.device_os = regForm.cleaned_data[Constants.PARA_DEVICEOS]
        user.device_token = regForm.cleaned_data[Constants.PARA_DEVICETOKEN]
        user.country_code = regForm.cleaned_data[Constants.PARA_COUNTRYCODE]
        user.language = regForm.cleaned_data[Constants.PARA_LANGUAGE]
        
        return_code = services.register_user(user)
        if return_code:
            return HttpResponse("error, code=" + return_code)

        return HttpResponse("ok")
    else:
        print regForm.errors
        return HttpResponse("error")

class RegForm(forms.Form):
    lid = forms.CharField(max_length=50)
    lty = forms.IntegerField()
    did = forms.CharField(max_length=150)
    dos = forms.IntegerField()
    cc = forms.CharField(max_length=20)
    lang = forms.CharField(max_length=20)
    dm = forms.CharField(max_length=50)
    dto = forms.CharField(max_length=150)
