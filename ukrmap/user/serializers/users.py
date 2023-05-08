from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from user.models.users import User
from organisation.models.organisations import Page,Employee

from django.db import transaction

################
##  REGISTRATION
################
class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True,
            validators=[UniqueValidator(queryset=User.objects.all())])

    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        # profile_data = validated_data.pop('user')
        with transaction.atomic():
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                role='admin'
            )
            user.set_password(validated_data['password'])
            user.save()
            page = Page.objects.create(admin=user)
            page.save()
            Employee.objects.create(page=page,user=user)
        return user

#####################
#  CHANGE PASS
####################
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_pass = serializers.CharField(write_only=True)
    new_pass = serializers.CharField(write_only=True)
    # new_pass2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('old_pass','new_pass')

    def validate(self, attrs):
        user = self.instance
        old_pass = attrs.pop('old_pass')
        if not user.check_password(old_pass):
            raise serializers.ValidationError({"password": "not corect"})

        return attrs
    
    def validate_new_pass(self,value):
        validate_password(value)
        return value
    
    def update(self,instance,validated_data):
        password = validated_data.pop('new_pass')
        instance.set_password(password)
        instance.save()

        return instance
    
########################
# ME USER
########################
class MeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','username')

########################
# ALL USERS
##########################
class UserListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = User
        fields = ('id','username','full_name')