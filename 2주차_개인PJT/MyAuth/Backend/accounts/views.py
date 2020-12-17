from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import UserSerializer

# Create your views here.
User = get_user_model()

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def retrieve_password(request):
    print("1111111", request.user)
    try:
        user = get_object_or_404(User, username = request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except:
        print('++++++s')
        return Response(serializer.data)