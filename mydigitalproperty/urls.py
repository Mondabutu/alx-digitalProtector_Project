
from django.urls import path
from . import views
 

urlpatterns = [

# Homepage Url
    path('', views.home, name='home'),
   # path('login/', views.login_user, name='login'),
   
# Log out Url
    path('logout/', views.logout_user, name='logout'),
    
# Register URL
    path('register/', views.register_user, name='register'),
    path('dashboard/', views.dashboard_user, name='dashboard'), 

# Record URL
    path('record/', views.property_lists, name='record'), 
 
# Verify User URL.
    path('verify/', views.verify_user, name='verify'), 
   
]
