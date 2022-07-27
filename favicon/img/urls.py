from django.urls import path
from . import views


urlpatterns = [
    path('', views.imgOverview , name = "img-overview"),
    path('upload/', views.imgUpload , name = "img-upload"),
    
]