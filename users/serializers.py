from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Pet, FinderFormsModel

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number')
        read_only_fields = ('id', 'email')


class PetSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Pet
        fields = ('category', 'age', 'name', 'breed', 'lost_status', 'owner')
        read_only_fields = ('lost_status',)


class FinderFormsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = FinderFormsModel
        fields = ('phone_number', 'message', 'lat', 'lot', 'user')
        read_only_fields = ('lat', 'lot')
