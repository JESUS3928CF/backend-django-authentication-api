# from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

# / Importaciones necesarias
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# / Clase para obtener un token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims - la información encriptada del usuario
        token['username'] = user.username

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 


@api_view(['GET']) 
def getRoute(request):
    routes = [
        'api/token',
        'api/token/refresh'
    ]
    return Response(routes) #- Ya no usamos safe aca 