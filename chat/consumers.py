import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Joindre le groupe
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Quitter le groupe
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Reçoit un message envoyé par le client et le diffuse à tous les membres de la salle.
        """
        try:
            data = json.loads(text_data)
            message = data.get('message', '')

            # Diffuser le message au groupe
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        except Exception as e:
            print(f"Erreur dans receive: {e}")

    async def chat_message(self, event):
        """
        Diffuse un message reçu du groupe à ce client WebSocket.
        """
        message = event['message']

        # Envoyer le message au client WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
