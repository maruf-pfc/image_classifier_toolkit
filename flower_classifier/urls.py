from django.urls import path
from . import views

app_name = "flower_classifier"

urlpatterns = [
    path('', views.predict_flower, name="predict_flower"),
]
