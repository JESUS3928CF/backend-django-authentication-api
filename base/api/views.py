from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import NoteSerializer
from base.models import Note

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

#/ Importaciones necesarias
from .serializers import UserRegistrationSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import permissions

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



#/ Endpoint para registrar un usuario
class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]  # Permite a cualquiera acceder a esta vista

    def perform_create(self, serializer):
        serializer.save()



@api_view(['GET']) 
def getRoute(request):
    routes = [
        'api/token',
        'api/token/refresh'
    ]
    return Response(routes) #- Ya no usamos safe aca 


@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def getNotes(request):
    #/ Obteniendo solo las notas del usuario autenticado
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

