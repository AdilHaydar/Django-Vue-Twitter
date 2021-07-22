from ..models import Profile

from rest_framework import serializers

class ProfilSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only= True)
    foto = serializers.ImageField(read_only = True)

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileFotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['foto']