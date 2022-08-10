from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 
from .views import Index
from . import views 
from .views import nosotros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),

    path('Noticias/', include('apps.Noticias.urls') , name = 'home'),

    path('nosotros/', nosotros, name='nosotros'),

    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

