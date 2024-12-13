import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MuscleTrackerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')

        # Echo the message back
        await self.send(text_data=json.dumps({
            'message': f'Received: {message}'
        }))
