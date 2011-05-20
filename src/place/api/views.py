from django import forms
from orange.django.place.utils import get_json_response
from orange.place import errors
from place.api import MethodConsts
from place.api.utils import get_return_dict
import logging
import place.api.methods
import traceback


logger = logging.getLogger(__name__)

def internal_method(request):
    if request.method == 'GET':
        in_form = InternalForm(request.GET)
        logger.info('[RECV] %s' % in_form.data)
        if in_form.is_valid():
            try:
                method = getattr(place.api.methods, in_form.cleaned_data[MethodConsts.METHOD])
                return method(request)
            except Exception:
                returnCode = errors.ERROR_PARA_METHOD_NOT_FOUND
                logger.exception('%s', traceback.extract_stack())
                return get_json_response(get_return_dict(returnCode, message='unknown error'))
        else:
            returnCode = errors.ERROR_PARAMETER
            return get_json_response(get_return_dict(returnCode, message=in_form.errors))
    else: 
        returnCode = errors.ERROR_NOT_GET_METHOD
        return get_json_response(get_return_dict(returnCode, message='not GET method'))

class InternalForm(forms.Form):
    fields = MethodConsts.METHOD + '= forms.CharField(max_length=10)'    
    code = compile(fields, '', 'exec')
    exec(code)
