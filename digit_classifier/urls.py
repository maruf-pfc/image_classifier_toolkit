from django.urls import path
from . import views

app_name = "digit_classifier"

urlpatterns = [
    path('', views.predict_digit, name="predict_digit"),
]
