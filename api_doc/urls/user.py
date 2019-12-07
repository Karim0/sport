from django.urls import path
from api_doc import views

urlpatterns = [
    path('authUser/', views.authUser),
    path('buyGymMembership', views.buyGymMembership),
    path('addOrderFoodDelivery', views.addOrderFoodDelivery)
]
