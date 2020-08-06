from django.urls import path
from app_tiendanaru import views




urlpatterns = [
    
    path('', views.home,name="Home"),
    path('bienestar_nutricion', views.bienestar_nutricion,name="bienestar_nutricion"),
    path('corporal_facial', views.corporal_facial,name="corporal_facial"),
    path('aseo_personal', views.aseo_personal,name="aseo_personal"),
    path('maquillaje_perfumeria', views.maquillaje_perfumeria,name="maquillaje_perfumeria"),
    path('contacto', views.contacto,name="contacto"),
    path('gracias', views.gracias,name="gracias"),
    
   
    
]