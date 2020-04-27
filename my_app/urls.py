from django.conf.urls import url
from . import views

#set the namespace
#app_name = 'my_app'
 
urlpatterns = [
   #url('', views.index, name='index'),
   url('biology/', views.biology, name='biology'),
   url('geometry/', views.geometry, name='geometry'),
   url('martial_arts/', views.martial_arts, name='martial_arts'),
   url('math/', views.math, name='math'),
   url('physics/', views.physics, name='physics'),
]
