from django.shortcuts import render

from . models import Department,Doctor
from . forms import BookingForm
# Create your views here.

numbers ={
    'num1': 0,
    
 }
 
def index(request):
   return render(request,'index.html', numbers)


def doctors(request):
   doctors = Doctor.objects.all()
   return render(request,'doctors.html', {'dict_doc' : doctors})  
 


def about(request):
   return render(request,'about.html')

def booking(request):
   form = BookingForm()
   if request.method == 'POST':
      form =BookingForm(request.POST)
      if form.is_valid():
         form.save()
     
      form = BookingForm()

   return render(request,'booking.html', {'form': form})
   


def contact(request):
   return render(request,'contact.html')

def department(request):
   departments = Department.objects.all()
  
   return render(request,'department.html', {'dict_dept' : departments})