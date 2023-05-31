from django.shortcuts import render
from rest_framework import generics

from .models import Menu
from .models import MenuItem
from django.core import serializers
from .serializers import MenuSerializer
from .serializers import MenuItemSerializer

from rest_framework.decorators import api_view
from .models import Booking
from datetime import datetime
import json
from .forms import BookingForm

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# function to return home page.
def home(request):
 return render(request, 'index.html', {})

# function to return about page view
def about(request):
    return render(request, 'about.html')

# function to make a reservation
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# function to display menu items list
@api_view()
@permission_classes([IsAuthenticated])
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

# function to display single menu item
def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

# function to view bookings
def bookings(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    #booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings": bookings, "date": date})

