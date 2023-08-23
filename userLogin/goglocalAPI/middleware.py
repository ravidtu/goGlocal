from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
JWT_authenticator = JWTAuthentication()
import logging
import json
logger = logging.getLogger(__name__)

class ProcessRequestMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """
        Middleware to check token and append it in the request if valid 
        """
        if not request.user.is_authenticated:
            token = None
            token = request.headers.get('authorization', None)
            logger.info(f"request received for endpoint {str(request.path)}")
            if token:
                try:
                    response = JWT_authenticator.authenticate(request)
                    if response is not None:
                        user , token = response
                        request.user = user
                    else:
                        response = {"message": "Authorization not found, Please send valid token in headers"}
                        logger.info(f"Response {response}")
                        return HttpResponse(json.dumps(response), status=401)
                except:
                       response = {"message": "invalid token, Please send valid token in headers"}
                       logger.info(f"Response {response}")
                       return HttpResponse(json.dumps(response), status=401)