
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from organisation.models.organisations import Group,Page
import pdb
from django.db import transaction
from django.db.models import Q
from organisation.serializers.mixins import UserEmployeeSerializer

from crum import get_current_user


###########
## GROUP
###########
class GroupListSerializer(serializers.ModelSerializer):
    created_by = UserEmployeeSerializer()
    class Meta:
        model = Group
        exclude = ('page',)
        read_only_fields = ("created_at","updated_at","created_by","update_by")


class GroupRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ("created_at","updated_at","created_by","update_by")


###########################
#   CREATE
###########################
class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name',)
        read_only_fields = ("created_at","updated_at","created_by","update_by")

    def validate(self, attrs):
        user = get_current_user()
        page = Page.objects.filter(Q(admin=user) | Q(employees=user)).first()

        if self.Meta.model.objects.filter(
                page=page, name=attrs['name']
        ).exists():
            raise ParseError(
                'duplicate name group'
            )
        
            # e.response.data.error - to react
            # raise serializers.ValidationError({"error": "duplicate name group"})

        return attrs
    
    def create(self, validated_data):
        user = get_current_user()
        page_name = Page.objects.filter(Q(admin=user) | Q(employees=user)).first()
        group = Group.objects.create(name=validated_data['name'],page=page_name)
        return group
    
    def to_representation(self,instance):
        
        data = super(GroupCreateSerializer, self).to_representation(instance)
        data['id'] = instance.id
        data['name'] = instance.name
        data['created_by'] = instance.created_by.username
        data['created_at'] = instance.created_at

        return data

#############################
#   UPDATE
#############################
class GroupUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
        )
    def validate(self, attrs):
        user = get_current_user()
        page = Page.objects.filter(Q(admin=user) | Q(employees=user)).first()

        if self.Meta.model.objects.filter(
                page=page, name=attrs['name']
        ).exists():
            raise ParseError(
                'duplicate name group'
            )
    # def validate(self, attrs):
    #     # Check name duplicate
    #     if self.instance.name == attrs['name']:
    #         raise ParseError(
    #             'duplicate name group'
    #         )
        return attrs