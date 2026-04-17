from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

numbers ={
    'num1': 0,
    
 }
 
def index(request):
   return render(request,'index.html', numbers)


def doctors(request):
   return render(request,'doctors.html')


def about(request):
   return render(request,'about.html')

def booking(request):
   return render(request,'booking.html')

def contact(request):
   return render(request,'contact.html')

def department(request):
   return render(request,'department.html')