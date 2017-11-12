# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# Create your views here.


class Image(APIView):
	"""
	CRUD for Images
	"""
	authentication_classes = ()
	permission_classes = ()
