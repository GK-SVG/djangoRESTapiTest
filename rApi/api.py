from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .slzr import *

class Userlist(APIView):
    def get(self,request):
        model = User.objects.all()
        serializer = UserSerializer(model,many=True)
        return Response(serializer.data)