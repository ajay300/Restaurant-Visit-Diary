from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth import authenticate
from app.models import ContactUs
#api
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ContactSerializers, SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializers, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializers
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import  ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView



from api import serializers


# Generate Token manually.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Registration From API
class UserRegistrationView(APIView):
    renderer_class = [UserRenderer]
    def post(self , request , format=None):
        serializer = UserRegistrationSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'msg':'Registration successful','token':token})
        return Response(serializer.errors)


class UserLoginView(APIView):
    renderer_class = [UserRenderer]
    def post(self , request , format=None):
        serializer = UserLoginSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                res = {'msg':'SuccessFully Login','token':token}
                return Response(res.values() , status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}},status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)


# ====================
# For Contact serializer View

# Concrete View : ListAPIView + UpdateAPIView = ListCreateview 
class ContactListcreate(ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializers

class ContactRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializers

class ContactRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializers