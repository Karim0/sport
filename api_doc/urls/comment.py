from django.urls import path
from api_doc import views

urlpatterns = [
    path("getAllComment", views.getAllComment),
    path("getCommentById/<int:pk>", views.getCommentById),
    path("updateComment/<int:pk>", views.updateComment),
    path("deleteComment/<int:pk>", views.deleteComment),
    path("addComment", views.addComment),
    # path("addCommentToCoach/", views.addCommentToCoach),
    # path("updateCommentToCoach/<int:pk>", views.updateCommentToCoach),
    # path("deleteCommentToCoach/<int:pk>", views.deleteCommentToCoach),
]
