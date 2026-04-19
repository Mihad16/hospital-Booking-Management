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
        return self.doc_name