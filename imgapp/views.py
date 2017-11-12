# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from imgapp.models import Image
from imgapp.serializers import ImageSerializer
# Create your views here.


class ImageView(APIView):
	"""
	CRUD for Images
	"""
	model = Image
	serializer_class = ImageSerializer

	def get_queryset(self):
		""" Return Image belonging to the current user"""
		queryset = self.model.objects.all()
		queryset = queryset.filter(user=self.request.user)
		return queryset

	def perform_create(self):
		""" Associate current user as image owner """
		return serializer.save(user=self.request.user)
