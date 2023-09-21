from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import NoteSerializer
from base.models import Note

# ! Lee
# /- Esto es solo los usuarios autenticados tengan acceso a ciertas vistas o recursos.
from rest_framework.permissions import IsAuthenticated
# / Importando el decorador de permission_classes 
from rest_framework.decorators import api_view, permission_classes


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

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


@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def getNotes(request):
    #/ Obteniendo solo las notas del usuario autenticado
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)