
from django.contrib import admin
from django.urls import path, include
from .views import companyviewset,employeeviewset,positionviewset,divisionviewset,departmentviewset
from rest_framework import routers


# rourter provide an easy way of automatically determining the URL conf
router= routers.DefaultRouter()
router.register(r'companies',companyviewset)
router.register(r'employees',employeeviewset)
router.register(r'divisions', divisionviewset)
router.register(r'departments', departmentviewset)
router.register(r'positions', positionviewset)


urlpatterns = [
    path ('',include(router.urls))

   
]
