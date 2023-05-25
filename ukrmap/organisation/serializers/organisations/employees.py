from rest_framework import serializers
from organisation.models.organisations import Employee
import pdb
from django.db import transaction
from organisation.serializers.mixins import UserEmployeeSerializer,User,Page,UserShortSerializer

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



#####################
## EMPLOYEE
#####################
class OrganisationEmployeeRetriverSerializer(serializers.ModelSerializer):
    # user = UserEmployeeSerializer()
    # page = PageShortSerializer()
    # position = PositionShortSerializer()
    class Meta:
        model = Employee
        fields = ('id','user','page')

#update
class OrganisationEmployeeUpdateSerializer(serializers.ModelSerializer):
    user = UserShortSerializer()
    class Meta:
        model = Employee
        fields = ('id','user',)

    
    def update(self,instance, validated_data):
        user_data = validated_data.pop('user') if 'user' in validated_data else None
        with transaction.atomic():
            instance = super().update(instance,validated_data)

            if user_data:
                user = instance.user

                profile_serializer = UserShortSerializer(instance=user,
                                                    data=user_data,
                                                    partial=True) # дозволено частковий апдейт
                profile_serializer.is_valid(raise_exception=True)
                profile_serializer.save()

        return instance

# list
class OrganisationEmployeeListSerializer(serializers.ModelSerializer):
    user = UserEmployeeSerializer()
    # position = PositionShortSerializer()
    class Meta:
        model = Employee
        fields = ('id','user',)

# Create
class OrganisationCreateEmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
            required=True,write_only=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    role = serializers.CharField(write_only=True)
    class Meta:
        model = Employee
        fields = ('username','password','password2','email','role')


    
    #  перевірка перед створенням користувача організації 
    #  чи є власником організації
    def validate(self,attrs):
        role = ['admin','manager','member']

        if attrs['role'] not in role:
            raise serializers.ValidationError({"role": "error role"})

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        current_user = self.context['request'].user
        # current_user = get_current_user()

        page = Page.objects.filter(admin = current_user).first()

        if not page:
            raise serializers.ValidationError({"error": "Page not faund or user not director"})
        
        attrs['page'] = page
        return attrs
    
    def create(self, validated_data):
        user = self.context['request'].user

        with transaction.atomic():
            page_name = Page.objects.filter(
                admin=user).first()
            # position_name = Position.objects.filter(
            #     name=validated_data['position']).first()
            # pdb.set_trace()
            # if not page_name or not position_name:
            #     raise serializers.ValidationError({"error": "error organisation or position"})

            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                role=validated_data['role'],
            )
            user.set_password(validated_data['password'])
            # pdb.set_trace()
            user.save()

            employee = Employee.objects.create(user=user,page=page_name)
        return employee
    
    def to_representation(self,instance):
        
        data = super(OrganisationCreateEmployeeSerializer, self).to_representation(instance)
        data['id'] = instance.id
        data['user'] = instance.user.username
        data['page'] = instance.page.admin.username
        data['role'] = instance.user.role
        return data
    