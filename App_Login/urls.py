from django.urls import path
from App_Login import views
app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user_profile/', views.user_profile, name='user_profile'),
]
