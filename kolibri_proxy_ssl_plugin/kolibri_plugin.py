from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django.conf import settings
from kolibri.plugins import KolibriPluginBase
# from kolibri.plugins.hooks import register_hook
# from kolibri.plugins.user import hooks


class OpenIDConnect(KolibriPluginBase):
    django_settings = "settings"

