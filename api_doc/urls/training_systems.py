from django.urls import path
from api_doc import views


urlpatterns = [
    path("getAllTrainingSystems", views.getAllTrainingSystems),
    path("getTrainingSystemsById/<int:pk>", views.getTrainingSystemsById),
]
