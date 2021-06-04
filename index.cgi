#!仮想環境のパス/bin/python3.7
import sys, os
 
#sys.path.insert(0, "仮想環境のパス/bin")
 
os.environ['DJANGO_SETTINGS_MODULE'] = "config.settings"
 
from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
CGIHandler().run(application)