from django.urls import path
from api_doc import views

urlpatterns = [
    path("addCommentFood", views.addCommentFood),
    path("deleteCommentFood/<int:pk>", views.deleteCommentFood),
    path("getAllFood", views.getAllFood),
    path("updateCommentFood/<int:pk>", views.updateCommentFood),
    path("getFoodById/<int:pk>", views.getFoodById),
]
