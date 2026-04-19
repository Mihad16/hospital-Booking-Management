from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm (forms.ModelForm):
        class Meta:
            model=Booking
            fields= '__all__'



            widgets = {
                'appointment_date': DateInput(),   
                  }
            
            labels = {
                'p_name': 'Patient Name',   
                'p_email': 'Patient Email',
                'p_phone': 'Patient Phone', 
                'doc_name': 'Doctor Name',
                'appointment_date': 'Appointment Date',
                 }


