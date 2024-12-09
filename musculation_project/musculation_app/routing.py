from django.urls import path
from musculation_app.consumers import MuscleTrackerConsumer

websocket_urlpatterns = [
    path('ws/muscle_tracker/', MuscleTrackerConsumer.as_asgi()),
]
