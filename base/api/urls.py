from django.urls import path
from . import views

from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import  (
    TokenRefreshView
)

urlpatterns = [
    path('', views.getRoute),
    path('notes/', views.getNotes),  # Corregido: Asignar la vista getNotes a la URL
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # / Usando en el endpoint
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),    
]
