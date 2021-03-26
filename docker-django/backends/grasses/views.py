from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import GrassSerializer
from .models import Grass


# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def grass_create_read(request):
    if request.method == 'GET':
        grasses = Grass.objects.filter(user=request.user)
        serializer = GrassSerializer(grasses, many =True)
        return Response(serializer.data)
    else:
        serializer = GrassSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user= request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)