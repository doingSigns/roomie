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
    path('rooms/list', views.room_list, name='room_list'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('rooms/new/', views.room_create, name='room_create'),
    path('rooms/<int:pk>/edit/', views.room_update, name='room_update'),
    path('rooms/<int:pk>/delete/', views.room_delete, name='room_delete'),
    path('preference/', views.preference_form, name='preference_form'),
    path('preference2/', views.preference_form2, name='preference_form2'),
    #path('login/', auth_views.LoginView.as_view(template_name='web/registration/login.html'), name='web:login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # ... other URLs
    path('matches/', views.matches, name='matches'),
]
