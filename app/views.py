# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializer import UserSerializer
from .models import User


# Create your views here.


class UserView(APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"Users": serializer.data}, status=200)

    def post(self, request, *args, **kwargs):
        user = request.data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"success": "User '{}' created successfully".format(user["name"])}, status=201)