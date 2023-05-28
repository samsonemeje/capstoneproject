from django.contrib import admin 
from django.urls import path 
from . import views
  
urlpatterns = [ 
    # path('alternateindex', views.alternateindex, name='alternateindex'),
    path('', views.home, name='home'),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('booking/', views.booking, name="booking"),
]
