from django.urls import path
from api_doc import views

urlpatterns = [
    path("getAllCoach/", views.getAllCoach),
    path("getCoachesBySectionId/<int:pk>", views.getCoachesBySectionId),
    path("addCommentToCoach/", views.addCommentToCoach),
    path("updateCommentToCoach/<int:pk>", views.updateCommentToCoach),
    path("deleteCommentToCoach/<int:pk>", views.deleteCommentToCoach),
    path("getCommentByCoachId/<int:pk>", views.getCommentByCoachId),
]
