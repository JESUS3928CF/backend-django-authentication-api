from django.urls import path
from . import views

# / Ahora revivimos la vista que nos retorna el token con la info del usuario
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import  (
    # TokenObtainPairView, #- Ya no se obtiene por defecto
    TokenRefreshView
)

urlpatterns = [
    path('', views.getRoute),
    
    # / Usando en el endpoint
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')    
]
