from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import company,employee, division, department, position
from .serializers import companyserializers,employeeserializers,divisionSerializer,departmentSerializer,positionSerializer

class divisionViewSet(viewsets.ModelViewSet):
  queryset = division.objects.all()
  serializer_class = divisionSerializer

class departmentviewset(viewsets.ModelViewSet):
  queryset=department.objects.all()
  serializer_class=departmentSerializer

class positionviewset(viewsets.ModelViewSet)::
  queryset=position.objects.all()
  serializer_class=positionSerializer

# Create your views here.
class companyviewset(viewsets.ModelViewSet): #ViewSet gets control (THIS CLASS) companyviewset
  queryset=company.objects.all() 
  serializer_class=companyserializers

  #company/{company_id}/employees/
  # to get employees of a particular company
  @action(detail=True,methods=['get'])
  def employees(self,response,pk=None):
    comp=company.objects.get(pk=pk)
    emps=employee.objects.filter(company=comp)
    emps_serializer=employeeserializers(emps,many=True,context={'request':response.request})
    return Response(emps_serializer.data)



class employeeviewset(viewsets.ModelViewSet):
  queryset=employee.objects.all()
  serializer_class=employeeserializers

@action(detail=True, methods=['get'])
def departments(self, request, pk=None):
    depts = department.objects.filter(division__company_id=pk)
    serializer = departmentSerializer(depts, many=True)
    return Response(serializer.data)

class employeeviewset(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeserializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['company', 'department', 'position']
    search_fields = ['name', 'email']







