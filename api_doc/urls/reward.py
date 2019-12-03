from django.urls import path
from api_doc import views

urlpatterns = [
    path("addReward", views.addReward),
    path("deleteReward/<int:pk>", views.deleteReward),
    path("getAllReward", views.getAllReward),
    path("getRewardById/<int:pk>", views.getRewardById),
    path("updateReward/<int:pk>", views.updateReward),
]
