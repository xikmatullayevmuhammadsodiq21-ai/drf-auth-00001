from apps.users.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializers(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



class UserCreateSerializers(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'email', 'last_name', 'password']