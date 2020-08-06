from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):

    return render(request, "app_tiendanaru/home.html")

def bienestar_nutricion(request):

    
    return render(request, "app_tiendanaru/bienestar_nutricion.html")

def corporal_facial(request):

   return render(request, "app_tiendanaru/corporal_facial.html")

def aseo_personal(request):

    return render(request, "app_tiendanaru/aseo_personal.html")

def maquillaje_perfumeria(request):

    return render(request, "app_tiendanaru/maquillaje_perfumeria.html")



def gracias(request):

    return render(request, "app_tiendanaru/gracias.html")

def contacto(request):

    if request.method=="POST":#cuando le damos enviar me pasa a esta vista

        subject=request.POST["first-name"]+" "+ request.POST["last-name"]#con estas variables tomamos lo que escribieron en lso campos de contacto
        message=request.POST["message"]+" "+ request.POST["email"]+" "+ request.POST["phone"]
        email_from=settings.EMAIL_HOST_USER#este seria el email que tenemos en settings
        recipient_list=["tiendanarupas@gmail.com"]#el correo donde quiero recbir el mensaje
        send_mail(subject,message,email_from,recipient_list)#tenemos que importar librearia mail y core settings

        return render(request, "app_tiendanaru/gracias.html")
        
    return render(request, "app_tiendanaru/contacto.html")





