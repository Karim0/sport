from django.urls import path
from . import views

urlpatterns = [
    path('getAllSportSection/', views.getAllSportSection),
    path('getSportSectionById/', views.getSportSectionById),
    path('deleteSportSection/<int:pk>', views.deleteSportSection),
    path('updateSportSection/', views.updateSportSection)
]
