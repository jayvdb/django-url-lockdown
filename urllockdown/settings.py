# -*- coding: utf-8 -*-
"""
"""
from django.conf import settings
"""
URL_LOCKDOWN = {
    'ENABLED': False,
    'SESSION_KEY': 'urllocks-allow',
}

"""

LOCKDOWN = getattr(settings, 'URL_LOCKDOWN', {})

ENABLED = LOCKDOWN.get('ENABLED', False)

SESSION_KEY = LOCKDOWN.get('SESSION_KEY', 'urllocks-allow')
