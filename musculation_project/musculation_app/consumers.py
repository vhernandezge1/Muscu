import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MusculationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Lorsqu'un client se connecte, accepte la connexion WebSocket
        self.room_name = "musculation"
        self.room_group_name = f"musculation_{self.room_name}"

        # Rejoindre un groupe WebSocket
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Lorsque le client se déconnecte, quitte le groupe
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Recevoir un message du client WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envoyer le message à tous les clients dans le groupe WebSocket
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Recevoir un message du groupe WebSocket
        message = event['message']

        # Envoyer le message au WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
