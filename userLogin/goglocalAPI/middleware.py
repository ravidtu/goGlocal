from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
JWT_authenticator = JWTAuthentication()

class ProcessRequestMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if not request.user.is_authenticated:
            token = None
            if "Authorization" in request.headers:
                token = request.headers["Authorization"]
            
            if token:
                try:
                    response = JWT_authenticator.authenticate(request)
                    if response is not None:
                        user , token = response
                        request.user = user
                    else:
                        return HttpResponse('Unauthorised', status=401)
                except:
                       return HttpResponse('invalid token', status=401) 