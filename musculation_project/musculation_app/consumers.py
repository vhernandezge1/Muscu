import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MuscleTrackerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accepter la connexion
        await self.accept()

    async def disconnect(self, close_code):
        # Gérer la déconnexion
        pass

    async def receive(self, text_data):
        # Traiter les messages reçus du client
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Répondre au client
        await self.send(text_data=json.dumps({
            'message': f"Reçu : {message}"
        }))
