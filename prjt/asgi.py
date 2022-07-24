"""
ASGI config for prjt project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from application import consumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prjt.settings')

websocket_urlPattern = [
    path('ws/polData',consumer.DashConsumer),
]
application = ProtocolTypeRouter({
    # 'http':

    'websockets':AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})
