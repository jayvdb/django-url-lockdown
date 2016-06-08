# -*- coding: utf-8 -*-
"""
"""
import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class LockPage(models.Model):
    title = models.CharField(_('Title'), max_length=512, blank=True, null=True)
    text = models.TextField(_('Text'), blank=True, null=True)
    error = models.TextField(_('Error Message'), blank=True, null=True)

    def __unicode__(self):
        return self.title


class URL(models.Model):
    pattern = models.CharField(_('URL Pattern'), max_length=512)
    password = models.CharField(_('Password'), max_length=512)
    lockpage = models.ForeignKey(LockPage)

    def __unicode__(self):
        return self.pattern
