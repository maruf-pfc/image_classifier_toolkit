from django.urls import path
from . import views

app_name = "vehicle_classifier"

urlpatterns = [
    path('', views.predict_vehicle, name="predict_vehicle"),
]
