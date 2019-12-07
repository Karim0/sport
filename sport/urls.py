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
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='API DOCUMENTATION')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='DOCUMENTATION FOR SPORT APPLICATION')),
    path('', include('sport_app.urls')),
    path('accounts/', include('rest_framework.urls')),

    #     Api doc
    path('sport_section/', include('api_doc.urls.sport_section')),
    path('comment/', include('api_doc.urls.comment')),
    path('raiting/', include('api_doc.urls.raiting')),
    path('location/', include('api_doc.urls.location')),
    path('coach/', include('api_doc.urls.coach')),
    path('food/', include('api_doc.urls.food')),
    path('achievement/', include('api_doc.urls.achievement')),
    path('reward/', include('api_doc.urls.reward')),
    path('training_systems/', include('api_doc.urls.training_systems')),
    path('usr/', include('api_doc.urls.user')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
