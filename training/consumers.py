import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Récupération du nom de la salle depuis l’URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # Joindre le groupe de la salle
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Quitter le groupe quand l’utilisateur ferme
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Réception d’un message du WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        username = data['username']
        message = data['message']

        # Envoyer à tout le groupe
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "username": username,
                "message": message
            }
        )

    # Réception depuis le groupe
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "username": event["username"],
            "message": event["message"]
        }))
