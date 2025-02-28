from django import forms
from .models import*

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        exclude = ['booked_on'] 

        labels={
            'cus_name':"Customer Name",
            'cus_phone'  : "Customer phone",
            'name'    :"event ",
            'booking date':"Booking Date",
        }