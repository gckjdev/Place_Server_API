from place.api.utils import Constants
import place.api.methods

def internal_method(request):
    if request.method == 'GET':
        methodName = request.GET[Constants.METHOD]
        method = getattr(place.api.methods, methodName)
        return method(request)

