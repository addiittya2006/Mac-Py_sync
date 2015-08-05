from django.db import models

# Create your models here.
# try:
from django.apps import apps
get_model = apps.get_model
# except ImportError:
#     from django.db.models.loading import get_model