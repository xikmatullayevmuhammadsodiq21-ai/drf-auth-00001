from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.users.serializers.auth_user import UserSerializers
from apps.users.models import User


class LoginView(APIView):

    def post(self, request):
        
        return Response({}, status=status.HTTP_200_OK)