from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('messages/', views.messages, name='messages'),
    path('favorite/', views.favorite_messages, name='favorite'),
    path('user/<str:username>/', views.send_message, name='send_message'),
    path('success/', views.success, name='success'),
    path('random/', views.random_message, name='random'),
    path('delete/<str:id>', views.delete_message, name='delete'),
    path('toggle-fav/<str:id>/', views.ToggleFavorite.as_view(), name='toggle-fav')
]
