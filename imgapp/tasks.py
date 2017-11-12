import os

from django.conf import settings
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from PIL import Image as PIL_Image

from imgapp.models import Image


@periodic_task(run_every=(crontab(minute='*/1')), name="compress_img", ignore_result=True)
def compress_img():
    # Lossless compression of image
	images = Image.objects.filter(compressed_image='')
	print images
	for image in images:
		try:
			filename = str(image.image)
			filename_split = filename.split('.')
			if len(filename_split) < 2:
				continue
			compressed_filename = str(filename_split[0]) + '_compressed.' + str(filename_split[1])
			file_path = os.path.join(settings.MEDIA_ROOT, filename)
			print file_path
			compressed_file_path = os.path.join(settings.MEDIA_ROOT, compressed_filename)
			im = PIL_Image.open(file_path)
			im.save(compressed_file_path, optimize=True, quality=30)
			image.compressed_image = compressed_filename
			# image.compressed_image.save(compressed_filename)
			image.save()
		except Exception as e:
			print e

