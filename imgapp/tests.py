# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

USERNAME = 'test'
PASSWORD = 'testpass'

# Create your tests here.
class ImageUploadTestCase(TestCase):

	def test_upload(self):
		"""
		Positive Test Case for Image Upload
		"""
		user = User.objects.create(username=USERNAME, password=PASSWORD)
		api_key=Token.objects.create(user=user)
		token = 'Token ' + str(api_key.key)
		auth_headers = {
    		'HTTP_AUTHORIZATION': token,
		}
		path = str(settings.STATIC_ROOT) + '/tests/test_sample.jpg'
		with open(path) as fp:
			resp = self.client.post('/image/', {'image': fp}, **auth_headers)
		self.assertEqual(resp.status_code, 201)

	def test_wrong_upload(self):
		"""
		Negative Test Case for Image Upload
		"""
		user = User.objects.create(username=USERNAME, password=PASSWORD)
		api_key=Token.objects.create(user=user)
		token = 'Token ' + str(api_key.key)
		token += 'ds'
		auth_headers = {
    		'HTTP_AUTHORIZATION': token,
		}
		path = str(settings.STATIC_ROOT) + '/tests/test_sample.jpg'
		with open(path) as fp:
			resp = self.client.post('/image/', {'image': fp}, **auth_headers)
		self.assertEqual(resp.status_code, 401)

	def test_list_of_images(self):
		"""
		Positive Test Case for Image Upload
		"""
		user = User.objects.create(username=USERNAME, password=PASSWORD)
		api_key=Token.objects.create(user=user)
		token = 'Token ' + str(api_key.key)
		auth_headers = {
    		'HTTP_AUTHORIZATION': token,
		}
		path = str(settings.STATIC_ROOT) + '/tests/test_sample.jpg'
		with open(path) as fp:
			resp = self.client.post('/image/', {'image': fp}, **auth_headers)
		self.assertEqual(resp.status_code, 201)
		resp = self.client.get('/image/', **auth_headers)
		data = resp.json()
		self.assertEqual(resp.status_code, 200)
		for one_data in data:
			pk = one_data.get('id', None)
			user = one_data.get('user', None)
			image = one_data.get('image', None)
			self.assertNotEqual(pk, None)
			self.assertNotEqual(user, None)
			self.assertNotEqual(image, None)

	def test_deletion_of_images(self):
		"""
		Positive Test Case for Image Upload
		"""
		user = User.objects.create(username=USERNAME, password=PASSWORD)
		api_key=Token.objects.create(user=user)
		token = 'Token ' + str(api_key.key)
		auth_headers = {
    		'HTTP_AUTHORIZATION': token,
		}
		path = str(settings.STATIC_ROOT) + '/tests/test_sample.jpg'
		with open(path) as fp:
			resp = self.client.post('/image/', {'image': fp}, **auth_headers)
		self.assertEqual(resp.status_code, 201)
		resp = self.client.get('/image/', **auth_headers)
		data = resp.json()
		self.assertEqual(resp.status_code, 200)
		for one_data in data:
			pk = one_data.get('id', None)
			user = one_data.get('user', None)
			image = one_data.get('image', None)
			self.assertNotEqual(pk, None)
			self.assertNotEqual(user, None)
			self.assertNotEqual(image, None)
			url = '/image/' + str(pk) + '/'
			resp = self.client.delete(url, **auth_headers)
			self.assertEqual(resp.status_code, 204)


