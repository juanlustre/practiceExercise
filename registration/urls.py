from django.urls import path
from . import views
app_name = "registration" 

urlpatterns = [
       path('api/register/', views.register_user, name='register_user'),
       path('api/users/', views.list_users, name='list_users'),  
       path('api/users/<int:pk>/', views.user_detail, name='user_detail'),
       
       path('login/', views.login_view, name='login_html'),
       path('logout/', views.logout_view, name='logout_html'),
       path('users/', views.users_html, name='users_html'),

       # HTML CRUD 
       path('users/add/', views.user_create_html, name='user_create_html'),
       path('users/<int:pk>/edit/', views.user_update_html, name='user_update_html'),
       path('users/<int:pk>/delete/', views.user_delete_html, name='user_delete_html'),
]