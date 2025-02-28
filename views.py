from django.shortcuts import render
from .models import Event
from .forms import BookingForm  # Import the form

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def events(request):
    dict_eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'events.html', dict_eve)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):

    # Booking form view 

    if request.method == 'POST':
        form = BookingForm(request.POST)  #  Use the form to process data
        if form.is_valid():
            form.save()                    #  Save form data to the database
    else:
        form = BookingForm()               #  Display an empty form for GET requests

    return render(request, 'booking.html', {'form': form})

from django.shortcuts import render

def chat_view(request):
    return render(request, 'chat.html')

