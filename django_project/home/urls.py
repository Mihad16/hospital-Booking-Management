
from django.urls import path
from . import views
urlpatterns = [
 
    path('',views.index),
     path('doctors/',views.doctors),
      path('about/',views.about),
       path('contact/',views.contact),
        path('department/',views.department),
        path('booking/',views.booking),
]   