from django.urls import path
from api_doc import views

urlpatterns = [
    path('getAllSportSection/', views.getAllSportSection),
    path('getSportSectionById/<int:pk>', views.getSportSectionById),
    path('getSportSectionType/', views.getSportSectionType),
    path('getSportSectionByTypeId/<int:pk>', views.getSportSectionByTypeId),
    # path('deleteSportSection/<int:pk>', views.deleteSportSection),
    # path('updateSportSection/', views.SportSection.updateSportSection),
]
