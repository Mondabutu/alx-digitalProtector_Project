
from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.home, name='home'),
   # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('dashboard/', views.dashboard_user, name='dashboard'), 

    path('record/', views.property_lists, name='record'), 
    path('verify/', views.verify_user, name='verify'), 
   
]
