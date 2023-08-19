from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('',views.home,name='home'),
]
