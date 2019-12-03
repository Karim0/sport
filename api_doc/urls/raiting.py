from django.urls import path
from api_doc import views

urlpatterns = [
    path("getAllRatings/", views.getAllRatings),
    path("getRatingById/<int:pk>", views.getRatingById),
    path("addRating/", views.addRating),
    path("deleteRating/<int:pk>", views.deleteRating),
    path("updateRating/<int:pk>", views.updateRating),
]
