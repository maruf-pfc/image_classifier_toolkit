from django.urls import path
from . import views

app_name = "human_emotion_classifier"

urlpatterns = [
    path('', views.predict_human_emotion, name="predict_human_emotion"),
]
