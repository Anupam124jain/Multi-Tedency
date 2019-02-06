from tenants.utils import tenant_db_from_request

from tenants.models import Tenant
from polls.models import Student
from rest_framework.views import APIView
from polls.serializers import StudentRegisterSerializer, StudentLoginSerializer, TenentRegisterSerializer
from tenants.models import Tenant

from rest_framework.response import Response
from rest_framework import status

class StudentRegistration(APIView):
    serializer_class = StudentRegisterSerializer
    def get(self, request):
        student = Student.objects.all()
        serializer = self.serializer_class(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id =  request.user.id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = user_id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentLogin(APIView):
    serializer_class = StudentLoginSerializer
    def get(self, request):
        student = Student.objects.all()
        serializer = self.serializer_class(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TenentRegistration(APIView):
    serializer_class = TenentRegisterSerializer
    def get(self, request):
        tenant = Tenant.objects.all()
        serializer = self.serializer_class(tenant, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)