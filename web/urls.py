from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views 
from web.forms import UserLoginForm

app_name = 'web'

urlpatterns = [
    path('', views.home, name='home'), 
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='web/login.html', authentication_form=UserLoginForm), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('preference/', views.preference_form, name='preference_form'),
    #path('login/', auth_views.LoginView.as_view(template_name='web/registration/login.html'), name='web:login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # ... other URLs
    path('matches/', views.matches, name='matches'),
]
