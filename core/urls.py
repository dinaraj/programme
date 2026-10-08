from django.contrib import admin
from django.urls import path

from programme import views


urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('', views.index, name='index'),
    path('d/<str:date>', views.index, name='index'),
]
