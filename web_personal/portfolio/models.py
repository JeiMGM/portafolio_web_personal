from django.db import models
from django.db.models.fields import DateTimeField
from django.forms import URLField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    description = models.TextField(max_length=200,verbose_name='Descripción')
    image=models.ImageField(upload_to="portfolio",verbose_name='imagen')
    link = models.URLField(max_length=200,verbose_name="Link de Enlace", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ('-created',)

    def __str__(self):
        return self.title
    

    
    
    