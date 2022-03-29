from rest_framework import serializers
from api_restt.models import Personal

class PersonalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personal
        fields = ['id', 'pid', 'nama', 'alamat']
