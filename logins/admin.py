# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import userDetails, posts

# Register your models here.
admin.site.register(userDetails)
admin.site.register(posts)
