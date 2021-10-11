from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import RegisterSerializer
from .renderers import UserRenderer
from .models import User
from .utils import Util
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
       
        return Response(user_data, status=status.HTTP_201_CREATED)
