from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from polls.models import Student
from tenants.models import Tenant

class StudentRegisterSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    tenant_id = serializers.CharField(read_only=True)
    user_id = serializers.CharField(read_only=True)
    # age = serializers.CharField(required=True, allow_blank=True, max_length=100)
    email = serializers.EmailField(required=True, allow_blank=True, max_length=100)
    password = serializers.CharField(required=True, style={'input_type': 'password'}, write_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)

class StudentLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=False, allow_blank=True, max_length=100)
    password = serializers.CharField(required=True, style={'input_type': 'password'}, write_only=True)

class TenentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['db_name',
                  'subdomain_prefix',
                  'company_name',
                  'company_email',
                  'role',
                  'country_code',
                  'mobile_no',
                  'industry',
                  'website_url',
                  'location',
                  'additional_info',
                  'contact_person'
                  ]
