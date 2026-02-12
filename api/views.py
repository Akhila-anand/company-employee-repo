from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import company, employee, division, department, position
from .serializers import (
    companyserializers,
    employeeserializers,
    divisionSerializer,
    departmentSerializer,
    positionSerializer
)


# ------------------ Division ViewSet ------------------

class divisionviewset(viewsets.ModelViewSet):
    queryset = division.objects.all()
    serializer_class = divisionSerializer


# ------------------ Department ViewSet ------------------

class departmentviewset(viewsets.ModelViewSet):
    queryset = department.objects.all()
    serializer_class = departmentSerializer


# ------------------ Position ViewSet ------------------

class positionviewset(viewsets.ModelViewSet):
    queryset = position.objects.all()
    serializer_class = positionSerializer


# ------------------ Company ViewSet ------------------

class companyviewset(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companyserializers

    # /company/{id}/employees/
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        comp = company.objects.get(pk=pk)
        emps = employee.objects.filter(company=comp)
        serializer = employeeserializers(
            emps, many=True, context={'request': request}
        )
        return Response(serializer.data)

    # /company/{id}/departments/
    @action(detail=True, methods=['get'])
    def departments(self, request, pk=None):
        depts = department.objects.filter(division__company_id=pk)
        serializer = departmentSerializer(depts, many=True)
        return Response(serializer.data)


# ------------------ Employee ViewSet ------------------

class employeeviewset(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeserializers

    # Filtering & Searching
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['company', 'department', 'position']
    search_fields = ['name', 'email']