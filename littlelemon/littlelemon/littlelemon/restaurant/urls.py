from django.urls import path, include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

  
urlpatterns = [ 
    path('', views.home, name='home'),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings/', views.bookings, name="bookings"),
    path('about/', views.about, name='about'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
