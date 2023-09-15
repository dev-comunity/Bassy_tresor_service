"""
ASGI config for Bassy_tresor_service project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
#from channels.auth import AuthMiddlewareStack
#from channels.routing import ProtocolTypeRouter, URLRouter
#from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

#from channels.routing import ProtocolTypeRouter
#from academie.rooting import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bassy_tresor_service.settings')

application =get_asgi_application()
#ProtocolTypeRouter({
#    'http':,
    
#}) 

