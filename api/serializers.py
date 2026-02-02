from rest_framework import serializers
from .models import company,employee, division, department, position


class divisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
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
         

'''
Serializer:Returns raw data (IDs, fields).Relationships are shown using primary keys
{
  "id": 1,
  "name": "Akhila",
  "course": 3
}
HyperlinkedModelSerializer:Returns data with hyperlinks to related resources
{
  "url": "http://api.com/students/1/",
  "name": "Akhila",
  "course": "http://api.com/courses/3/"
}
'''
