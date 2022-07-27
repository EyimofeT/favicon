from django.contrib import admin
from .models import User,AbstractUser
# Register your models here.

class profileAdmin(admin.ModelAdmin):
    list_display =[field.name for field in User._meta.fields]
admin.site.register(User,profileAdmin)