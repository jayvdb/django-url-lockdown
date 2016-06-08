# -*- coding: utf-8 -*-
"""
"""
from django import forms
from django.forms import forms
from django.forms import ModelForm

from urllockdown.models import URL


class URLForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = URL
        fields = ['password']
