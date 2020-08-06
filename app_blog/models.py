from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo=models.CharField('Titulo',max_length=200,blank=False,null=False)
    slug=models.CharField('slug',max_length=100,blank=False,null=False)
    descripcion = models.CharField('descripcion',max_length=600,blank=False,null=False)
    contenido=RichTextField()
    imagen=models.URLField(max_length=500,blank=False,null=False)
    fecha_creacion=models.DateField('fecha de creacion',auto_now=False,auto_now_add=True)
    
    class Meta:
        verbose_name ='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo




""" AQUI EMPEZAMOS HACER LA APP BLOG
1. creamos el modelo del post
2.hacemos la migraciones
3. la registramos en admin
4. instalamos pip install django-ckeditor y la registramos en settings apps
5. en modles importamos ckeditor"""