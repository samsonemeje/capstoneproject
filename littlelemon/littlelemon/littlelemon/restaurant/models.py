from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   id = models.PositiveIntegerField(primary_key = True)
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=5, decimal_places=2) 
   inventory = models.IntegerField() 

   def __str__(self):
      return self.title
