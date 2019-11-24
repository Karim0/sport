"""sport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'sport_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('test/', views.test, name='test'),
    # path('logout', views.logout1, name='logout')
    # path('login', views.LoginView.as_view(), name='login'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout1, name='logout'),
    path('coaches', views.coachView, name='coachView'),
    path('training_systems', views.trainingSystemView, name='systems'),
    path('search', views.search, name='search'),
]
