from rest_framework.serializers import ModelSerializer
from .models import Subject, User


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name',  'email', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class SubjectSerializers(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description',  'created_at', 'category', 'image']


