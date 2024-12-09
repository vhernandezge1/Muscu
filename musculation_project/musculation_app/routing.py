from django.urls import re_path
from musculation_app import consumers  

websocket_urlpatterns = [
    re_path(r'ws/muscle_tracker/', consumers.MuscleTrackerConsumer.as_asgi()),  
]
