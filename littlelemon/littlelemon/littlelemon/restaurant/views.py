from django.shortcuts import render
from django.http import HttpResponse

from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
# from .forms import BookingForm

# Create your views here.

def home(request):
 return render(request, 'index.html', {})

# def alternateindex(request):
#  return render(request, 'alternateindex.html', {})

# function to return about view
def about(request):
    return render(request, 'about.html')

# function to make booking by posting data
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# function to display menu items
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
def booking(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings": booking_json})
