from django.db import models

# Create your models here.


class Work_time(models.Model):
    address = models.CharField(max_length=30)
    ish_vaqti = models.DateTimeField()
    phone_number = models.CharField(max_length=15)
    facebook = models.URLField(max_length=50)
    instagram = models.URLField(max_length=50)

    def __str__(self):
        return self.address
    

class My_result(models.Model):
    years_experience = models.IntegerField(default = 0)
    expert_technicians = models.IntegerField(default= 0)
    satisfied_clients = models.IntegerField(default= 0)
    compleate_Projects= models.IntegerField(default= 0)
    
class Our_services(models.Model):
    services_name = models.CharField(max_length=200)
    services_about = models.CharField(max_length=200)


    def __str__(self):
        return self.services_name
    

class Contact(models.Model):
    name = models.CharField(max_length=20)
    services_namee = models.ForeignKey(Our_services,on_delete=models.CASCADE)
    email = models.EmailField(max_length=20)
    services_date = models.DateField()
    bio = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Our_expert(models.Model):
    name = models.CharField(max_length=20)
    facebook = models.URLField(max_length=50)
    instagram = models.URLField(max_length=50)
    img = models.ImageField(upload_to='images/')
    profeccion = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Our_clients(models.Model):
    client_name = models.CharField(max_length=15)
    client_services = models.ForeignKey(Our_services,on_delete=models.CASCADE)
    massage = models.CharField(max_length=100)



    
