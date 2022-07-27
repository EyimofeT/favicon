from django.contrib import admin
from .models import ImageUpload
# Register your models here.

class profileAdmin(admin.ModelAdmin):
    list_display =[field.name for field in ImageUpload._meta.fields]
admin.site.register(ImageUpload,profileAdmin)