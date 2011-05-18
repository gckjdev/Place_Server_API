from django import forms
from orange.django.place.utils import get_json_response
from place.api import errors
from place.api.methods.reg import get_return_dict
from place.api import MethodConsts
import place.api.methods

def internal_method(request):
    if request.method == 'GET':
        in_form = InternalForm(request.GET)
        if in_form.is_valid():
            method = getattr(place.api.methods, in_form.cleaned_data[MethodConsts.METHOD])
            return method(request)
        else:
            returnCode = errors.PARAM_ERROR
            return get_json_response(get_return_dict(returnCode, message=in_form.errors))

class InternalForm(forms.Form):
    m = forms.CharField(max_length=10)
