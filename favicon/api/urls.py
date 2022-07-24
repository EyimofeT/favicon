from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview , name = "api-overview"),
    path('user-list/', views.userList , name = "user-list"),
    path('user-search/<str:pk>', views.userSearch , name = "user-search"),
    path('signup/', views.userCreate , name = "user-create"),
    
    path('user-update/<str:pk>', views.userUpdate , name = "user-update"),
   path('user-delete/<str:pk>', views.userDelete , name = "user-delete"),
   path('login/', views.userLogin , name = "user-login"),
]