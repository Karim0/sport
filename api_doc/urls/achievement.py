from django.urls import path
from api_doc import views

urlpatterns = [
    path("addAchievement", views.addAchievement),
    path("deleteAchievement/<int:id>", views.deleteAchievement),
    path("getAllAchievement", views.getAllAchievement),
    path("updateAchievement/<int:id>", views.updateAchievement),
    path("getAchievementById/<int:id>", views.getAchievementById),
]
