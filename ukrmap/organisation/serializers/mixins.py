from rest_framework import serializers
from user.models.users import User
from organisation.models.organisations import Page,Employee

class ExtendedModelSerializer(serializers.ModelSerializer):

    class Meta:
        abstract = True

class DictMixinSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()

class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_active_account','role')

##################
# EMPLOYEE
##################
class EmployeeMixinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','user')

    def to_representation(self,instance):
        data = super(EmployeeMixinSerializer, self).to_representation(instance)
        data['user'] = instance.user.username

        return data

class UserEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','is_active_account','role')
        
class PageShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('name',)

class GeoInfoMixin(serializers.ModelSerializer):
    pass