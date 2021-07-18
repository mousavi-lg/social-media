from rest_framework.serializers import ModelSerializer
from .models import Profile


class Serializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
