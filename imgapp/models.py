# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.auth.models import User
from django.db import models

from imgapp.utils import get_upload_file_path
from rest_framework.authtoken.models import Token

# Create your models here.
class Image(models.Model):
	user = models.ForeignKey(User)
	image = models.ImageField(upload_to=get_upload_file_path)
	compressed_image = models.ImageField(upload_to=get_upload_file_path, blank=True, null=True)

	def __unicode__(self):
		return str(self.pk)
