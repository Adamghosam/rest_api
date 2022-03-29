from django.shortcuts import render
from rest_framework import viewsets,permissions
from api_restt.serializers import PersonalSerializer
from api_restt.models import Personal
# Create your views here.


class PersonalviewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

#
    # permission_classes = [permissions.IsAuthenticated]

