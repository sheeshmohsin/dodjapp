from django.contrib.auth.models import User

from rest_framework import serializers
from imgapp.models import Image


class ImageSerializer(serializers.ModelSerializer):
	user  = serializers.CharField(source='user.username',read_only=True)

	class Meta:
		model = Image
		fields = ('id', 'user', 'image', 'compressed_image')
