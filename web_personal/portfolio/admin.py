from atexit import register
from email.mime import image
from django.contrib import admin
from .models import Project


# Register your class here.

class project_admin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title","id", "link", "created", "updated", "image")
    search_fields = ("title",) 
 
    
# Register your models here.
admin.site.register(Project, project_admin)
