from django.shortcuts import render
from rest_framework import viewsets 
from .models import company,employee
from .serializers import companyserializers,employeeserializers
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class companyviewset(viewsets.ModelViewSet): #ViewSet gets control (THIS CLASS) companyviewset
    queryset=company.objects.all() 
    serializer_class=companyserializers

    #company/{company_id}/employees/

    # to get employees of a particular company
    @action(detail=True,methods=['get'])
    def employees(self,response,pk=None):
        company=company.objects.get(pk=pk)
        emps=employee.objects.filter(company=company)
        emps_serializer=employeeserializers(emps,many=True,context={'request':request})
        return Response(emps_serializer.data)



class employeeviewset(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=employeeserializers



#User hits an API URL
#GET /api/companies/
'''2️URL → Router → ViewSet → Model → Serializer → Response
In urls.py, DRF router connects the URL to companyviewset.
👉 Router decides which method to call:
GET → list()
POST → create()
PUT → update()
DELETE → destroy()

companyviewset:This is the brain/controller.It knows what data to take from the model and how to serialize it.
queryset :It knows what data to take
serializer_class:It knows how to serialize the data
The viewset interacts with the model to fetch data from the database using the queryset attribute. It then uses the serializer_class attribute to convert the data into a format suitable for API responses, such as JSON. Finally, it sends this serialized data back to the client as an HTTP response.
company.objects.all() :View talks to Model Fetches data from database
companyserializers:View sends data to Serializer Serializer:
Converts Model → JSON (for response)
Converts JSON → Model (for POST/PUT)

Response goes back to user

Finally, DRF sends:

[
  {
    "id": 1,
    "name": "ABC Company",
    "location": "Bangalore"
  }
]

URL → Router → ViewSet → Model → Serializer → JSON Response

User = Customer

ViewSet = Manager

Model = Database storage

Serializer = Translator

Response = Final answer
'''