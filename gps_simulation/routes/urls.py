from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin 



urlpatterns = [
    path('', views.home, name='home'),
    path('load/', views.load_graph, name='load_graph'),
    path('shortest-route/', views.shortest_route, name='shortest_route'),
    path('city/<int:id>/', views.city_detail, name='city_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)