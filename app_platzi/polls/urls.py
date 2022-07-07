from django.urls import path
# importamos algo del paquete actual que es polls
from . import views

urlpatterns = [
  path("", views.index, name = "index")
]