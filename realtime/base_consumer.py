import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser


class BaseConsumer(AsyncWebsocketConsumer):
    user = AnonymousUser()

    async def connect(self):
        self.user = self.scope.get("user", AnonymousUser())
        if self.user.is_authenticated:
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        pass

    async def send_json(self, data):
        await self.send(text_data=json.dumps(data))

    async def receive(self, text_data=None, bytes_data=None):
        pass  # Optional
