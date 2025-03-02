from django.conf.urls import patterns

urlpatterns = patterns('',)

import warnings
warnings.warn(
    "Django logtail urls no longer need adding to your project's urls.py. "
    "See the changelog for more details.",
    category=DeprecationWarning
)
