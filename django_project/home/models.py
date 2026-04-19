from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()


    def __str__(self):
        return self.dep_name


class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_specialty = models.CharField(max_length=100)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    dep_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr. ' +  self.doc_name + ' - ' + self.dep_name.dep_name
    
class Booking(models.Model):
    p_name = models.CharField(max_length=100)
    p_email = models.EmailField()
    p_phone = models.CharField(max_length=10)
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.p_name} - {self.doc_name.doc_name} - {self.appointment_date} {self.appointment_time}"