# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=100,null=False)