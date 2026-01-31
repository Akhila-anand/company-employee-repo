from django.db import models

# Create your models here.
# creating company model

class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    about=models.TextField()
    Type=models.CharField(max_length=50,choices=
                            (('IT','IT'),
                            ('Finance','Finance'),
                            ('Health','Health'),
                            ('Education','Education')
                            ))
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.name+"--"+self.location

#employee model
class employee(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(
                            ('manager','manager'),
                            ('developer','developer'),
                            ('tester','tester'),
                            ('hr','hr'),
                            ('team lead','team lead')))
    
    company=models.ForeignKey(company, on_delete=models.CASCADE)



