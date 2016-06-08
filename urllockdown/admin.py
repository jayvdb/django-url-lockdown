# -*- coding: utf-8 -*-
"""
"""
import logging

from django.contrib import admin

from .models import Access, URL, LockPage

# Get an instance of a logger
logger = logging.getLogger(__name__)


@admin.register(LockPage)
class LockPageAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('id', 'title', 'text', 'error')
    ordering = ['id', 'title', 'text', 'error']
    list_display_links = ('title',)
    list_editable = ('title', 'text', 'error')


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('pattern', )
    search_fields = ('id', 'pattern')
    ordering = ['id', 'pattern']
    list_display_links = ('pattern',)


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ('password', )
    search_fields = ('id', 'password')
    list_display_links = ('password',)

