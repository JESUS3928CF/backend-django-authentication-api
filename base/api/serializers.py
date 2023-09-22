# / Importaciones necesarias
from rest_framework.serializers import ModelSerializer
from base.models import Note
from django.contrib.auth.models import User

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

# / Creando el serializador
class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Asegúrate de incluir los campos necesarios

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user