from django.urls import path
from api_doc import views

urlpatterns = [
    path("addLocation", views.addLocation),
    path("getLocationBySectionId/<int:pk>", views.getLocationBySectionId),
    path("deleteLocation/<int:pk>", views.deleteLocation),
    path("updateLocation/<int:pk>", views.updateLocation),
]
