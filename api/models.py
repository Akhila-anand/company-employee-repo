from django.db import models

# Create your models here.
# creating company model

class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    about=models.TextField()
   
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.name+"--"+self.location

class division(models.Model):
    name=models.CharField(max_length=50)
    company=models.ForeignKey(company,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    division=models.ForeignKey(division,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class position(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


#employee model
class employee(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    is_active=models.BooleanField(default=True)

    position=models.ForeignKey(position,on_delete=models.SET_NULL,null=True,blank=True)
    
    department=models.ForeignKey(department,on_delete=models.SET_NULL,null=True,blank=True)

    
    company=models.ForeignKey(company, on_delete=models.CASCADE)



