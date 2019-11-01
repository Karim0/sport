from django.test import TestCase

# Create your tests here.
from django.core import management
import sport.settings as settings
management.setup_environ(settings)