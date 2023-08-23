# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class ProfileList(APIView):
    """
    A profile request which returns first name and last name.
    """
    def get(self, request, format=None):
            data = {'firstName': request.user.first_name,'lastName':request.user.last_name}
            return Response(data, status=status.HTTP_200_OK)