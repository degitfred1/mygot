from django.urls import path
from . import views

urlpatterns=[
path('has/',views.has),
path('lap/',views.lap),

]