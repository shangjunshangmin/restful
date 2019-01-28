# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2019/1/27 0027 下午 2:49'
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        password=instance.password
        instance.set_password(password)
        instance.save()

