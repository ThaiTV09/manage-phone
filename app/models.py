from django.db import models

# Create your models here.

class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=50 ,null=False, default='Công ty điện lực Quảng Trị')
    def __str__(self):
        return self.department
    
class Network(models.Model):
    network_id = models.CharField(primary_key=True, max_length=50)
    network = models.CharField(max_length=50 ,null=False, default='1')
    def __str__(self):
        return self.network

class System(models.Model):
    id = models.AutoField(primary_key=True)
    system = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.system)

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.status)

class Phone(models.Model):
    id = models.IntegerField (null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    serial = models.BigIntegerField(primary_key=True, blank=True)
    pack = models.CharField(max_length=255, null=True,blank=True)
    money = models.IntegerField(null=True,blank=True)
    date_connect = models.DateField(null=True,blank=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    date_join = models.DateField(null=True,blank=True)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE,blank=True,null=True)
    system_id = models.ForeignKey(System, on_delete=models.CASCADE,blank=True,null=True)
    network_id= models.ForeignKey(Network, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{str(self.serial)}, {self.phone}, {self.department_id}, {self.status_id}, {self.system_id}, {self.network_id}"

class PhoneItem(models.Model):
    id = models.AutoField(primary_key=True)
    serial = models.ForeignKey(Phone,on_delete=models.CASCADE,blank=True,null=True)
    date_use = models.DateField(null=True,blank=True)
    data = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.id)


