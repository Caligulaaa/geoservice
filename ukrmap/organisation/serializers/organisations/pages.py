
from rest_framework import serializers
from organisation.models.organisations import Page
import pdb
from django.db import transaction
from organisation.serializers.mixins import UserShortSerializer


class PageMySerializer(serializers.ModelSerializer):
    # employees = serializers.SlugRelatedField(many=True,read_only=True,slug_field='id')
    admin = UserShortSerializer()
    class Meta:
        model = Page
        exclude = ('employees',)