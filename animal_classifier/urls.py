from django.urls import path
from . import views

app_name = "animal_classifier"

urlpatterns = [
    path('', views.predict_animal, name="predict_animal"),
]
