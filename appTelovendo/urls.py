from django.urls import path
from  .views import *
from appTelovendo import *

app_name = 'app'


urlpatterns = [

    path('',index, name = 'index'),
    path('colaboracion/', colaboracion, name = 'colaboracion'),
    path('crearProveedor/',crearProveedor, name = 'crearProveedor'),
]