from django.test import TestCase, Client
from django.contrib.auth.models import User
from chat.models import Message
from django.urls import reverse
from channels.testing import WebsocketCommunicator
from chat.consumers import ChatConsumer
from fitness_project.asgi import application  
import json


class MessageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.message = Message.objects.create(content="Hello world!", sender=self.user, room="room1")

    def test_message_creation(self):
        """Test que le modèle Message est bien créé"""
        self.assertEqual(self.message.content, "Hello world!")
        self.assertEqual(self.message.sender.username, "testuser")
        self.assertEqual(self.message.room, "room1")


class ChatViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.message = Message.objects.create(content="Test message", sender=self.user, room="room1")

    def test_chat_page_access(self):
        """Test l'accès à la page de chat"""
        response = self.client.get(reverse('chat:room', kwargs={'room_name': 'room1'}))
        self.assertEqual(response.status_code, 200)

    def test_chat_message_display(self):
        """Test que les messages s'affichent dans la vue"""
        response = self.client.get(reverse('chat:room', kwargs={'room_name': 'room1'}))
        self.assertContains(response, "Test message")


class ChatWebSocketTest(TestCase):
    async def test_websocket_connection(self):
        """Test de connexion WebSocket et échange de messages"""
        communicator = WebsocketCommunicator(application, "/ws/chat/room1/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)

        # Envoie un message via WebSocket
        await communicator.send_json_to({
            "message": "Hello from WebSocket",
        })

        
        response = await communicator.receive_json_from()
        self.assertEqual(response, {
            "message": "Hello from WebSocket",
            "username": "Anonyme",  # Si non authentifié, le nom est "Anonyme"
        })

        # Ferme la connexion
        await communicator.disconnect()
