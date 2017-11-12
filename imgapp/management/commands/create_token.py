import getpass

from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework.authtoken.models import Token

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
	# Show this when the user types help
	help = "Command to create user and get token in response"

	# A command must define handle()
	def handle(self, *args, **options):
		success = True
		while success:
			try:
				username = str(raw_input('Username: '))
				password = getpass.getpass('Password: ')
				user = User.objects.create(username=username, password=password)
				api_key=Token.objects.create(user=user)
				success = False
				print "User Created Successfully with this token -> %s" % api_key.key
			except IntegrityError as e:
				if 'UNIQUE constraint failed: auth_user.username' in e.message:
					print "Username already exists, Please try again with different username"
				else:
					print (e)
			except Exception as e:
				print(e)