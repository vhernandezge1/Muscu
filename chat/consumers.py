import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print(f"Connecté à la room : {self.room_group_name}")

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f"Déconnecté de la room : {self.room_group_name}")

    async def receive(self, text_data):
        # Recevoir un message du WebSocket
        data = json.loads(text_data)
        message = data['message']

        print(f"Message reçu : {message}")

        # Envoyer le message au groupe
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Recevoir un message du groupe et l'envoyer au WebSocket
        message = event['message']
        print(f"Message envoyé aux clients : {message}")

        await self.send(text_data=json.dumps({
            'message': message
        }))
