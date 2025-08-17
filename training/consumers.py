import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "global_chat"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        # Message de bienvenue
        await self.channel_layer.group_send(self.room_group_name, {
            "type": "chat_message",
            "message": "🤖 Le chat est connecté. Dites bonjour !"
        })

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        if not text_data:
            return
        try:
            data = json.loads(text_data)
        except json.JSONDecodeError:
            data = {"message": text_data}
        message = (data.get("message") or "").strip()
        if not message:
            return
        user = self.scope["user"].username if self.scope["user"].is_authenticated else "Anonyme"
        await self.channel_layer.group_send(self.room_group_name, {
            "type": "chat_message",
            "message": f"{user}: {message}"
        })

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))
