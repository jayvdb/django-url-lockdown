# -*- coding: utf-8 -*-
"""
"""
import logging

from django.contrib import admin

from .models import URL, LockPage

# Get an instance of a logger
logger = logging.getLogger(__name__)


@admin.register(LockPage)
class LockPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'error')
    search_fields = ('id', 'title', 'text', 'error')
    ordering = ['id', 'title', 'text', 'error']
    list_display_links = ('title',)


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'password')
    search_fields = ('id', 'pattern', 'password')
    ordering = ['id', 'pattern']
    list_display_links = ('pattern', 'password')
