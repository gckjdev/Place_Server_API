from django import forms
from orange.django.place.utils import get_json_response
from place.api import MethodConsts, errors
from place.api.utils import get_return_dict
import logging
import place.api.methods

logger = logging.getLogger(__name__)

def internal_method(request):
    if request.method == 'GET':
        in_form = InternalForm(request.GET)
        logger.debug(in_form.data)
        if in_form.is_valid():
            method = getattr(place.api.methods, in_form.cleaned_data[MethodConsts.METHOD])
            return method(request)
        else:
            returnCode = errors.PARAM_ERROR
            return get_json_response(get_return_dict(returnCode, message=in_form.errors))
    logger.warn('internal method should not be posted')

class InternalForm(forms.Form):
    m = forms.CharField(max_length=10)
