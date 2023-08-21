from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
import jwt




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class UserList(APIView):
    def post(self, request, format=None):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    userObj = UserAPI.objects.get(email=serializer.initial_data['email'],password = serializer.initial_data['password'])
                except:
                    data = {'message': 'email or password is wrong'}
                    return Response(data,status=status.HTTP_200_OK)
                     
                return Response(get_tokens_for_user(userObj), status=status.HTTP_200_OK)
            data = {'message': 'bad request'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileList(APIView):
    def get(self, request, format=None):
            data = {'firstName': request.user.first_name,'lastName':request.user.last_name}
            return Response(data, status=status.HTTP_200_OK)