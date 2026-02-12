from rest_framework import serializers
from .models import company,employee, division, department, position


class divisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = division
        fields = '__all__'


class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = '__all__'


class positionSerializer(serializers.ModelSerializer):
    class Meta:
        model = position
        fields = '__all__'


class companyserializers(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model = company
        fields = '__all__'


class employeeserializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = employee
        fields='__all__'     
         


