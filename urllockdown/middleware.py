# -*- coding: utf-8 -*-
"""
"""
import re
from pydoc import locate

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from urllockdown.models import URL
from urllockdown import settings


class UrlLockdownMiddleware(object):
    """Middleware to password protect specific urls"""

    def __init__(self):
        """Initialize the middleware, by setting the configuration values.

        :param caching:
        """
        self.enabled = settings.ENABLED
        self.session_key = settings.SESSION_KEY

    def process_request(self, request):
        """Check if each request is allowed to access the current resource.

        :param request:
        :return:
        """

        # Allow request if django-url-lockdown is disabled.
        if not self.enabled:
            return None

        # If session is authorized, allow request
        if self.authorized(request):
            return None

        # If session is not authorized, try to authorize this session
        return self.authorize(request)

    def redirect(self, request):
        """Utility method to handle redirects."""
        url = request.path
        querystring = request.GET.copy()
        if self.logout_key and self.logout_key in request.GET:
            del querystring[self.logout_key]
        if querystring:
            url = '%s?%s' % (url, querystring.urlencode())
        res = HttpResponseRedirect(url)
        res['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
        return res

    def authorized(self, request):
        """Returns True if the user is authorized to view this URL.

        :param request: The request object
        :return: Bool
        """
        return False

    def authorize(self, request):
        """Sets the session cookie to authorize this user session.

        :param request: The request object
        :return: Bool
        """
        res = render_to_response('urllockdown/form.html', {},
                                 context_instance=RequestContext(request))
        #return HttpResponseRedirect('/cybint')

        urls = URL.objects.all()
        for url in urls:
            print url, request.path
            if url.pattern == request.path:

                return res




        return None

    def get_session(self, request):
        try:
            session = request.session
        except AttributeError:
            raise ImproperlyConfigured('django-url-lockdown requires the Django sessions framework')

        return session

    def process_response(self, request, response):
        """Processes the response object.

        :param request:
        :param response:
        :return: response
        """
        return response






