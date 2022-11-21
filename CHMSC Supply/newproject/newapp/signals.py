from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
import qrcode
import PIL
import pyqrcode
