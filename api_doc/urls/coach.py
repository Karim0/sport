from django.urls import path
from api_doc import views

urlpatterns = [
    path("getAllCoach/", views.getAllCoach),
    path("getCoachesBySectionId/<int:pk>", views.getCoachesBySectionId),
    path("getCommentByCoachId/<int:pk>", views.getCommentByCoachId),
]
