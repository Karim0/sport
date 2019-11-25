from django.urls import path
from api_doc import views

urlpatterns = [
    path("addAchievement", views.addAchievement),
    path("deleteAchievement/<int:pk>", views.deleteAchievement),
    path("getAllAchievement", views.getAllAchievement),
    path("updateAchievement/<int:pk>", views.updateAchievement),
    path("getAchievementById/<int:pk>", views.getAchievementById),
]
