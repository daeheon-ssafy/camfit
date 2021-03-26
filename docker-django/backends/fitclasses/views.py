from django.shortcuts import render

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import FitclassSerializer
from .models import Fitclass

@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def fitclass_list_create(request):
    if request.method == 'GET':
        fitclasses = Fitclass.objects.order_by('-pk')
        serializer = FitclassSerializer(fitclasses, many=True)
        return Response(serializer.data)
    else:
        if request.user.category == 1 or request.user.is_superuser:
            serializer = FitclassSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('트레이너만 클래스 생성 가능합니다')


@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def participate_left(request,fitclass_pk):
    fitclass = get_object_or_404(Fitclass, pk=fitclass_pk)
    serializer = FitclassSerializer(fitclass)

    # if 제한인원
    if fitclass.guests.filter(pk=user.pk).exists():
        fitclass.guests.remove(user)
    else:
        fitclass.guests.add(user)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save
    #asdf
