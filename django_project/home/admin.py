from django.contrib import admin
from . models  import Department, Doctor, Booking

# Register your models here.
admin.site.register(Department)

class DoctorAdmin(admin.ModelAdmin):
    list_display =('doc_name', 'doc_specialty', 'dep_name' , 'dep_image')
admin.site.register(Doctor,DoctorAdmin)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'p_email', 'p_phone', 'doc_name', 'appointment_date', 'appointment_time')
    
admin.site.register(Booking, BookingAdmin)