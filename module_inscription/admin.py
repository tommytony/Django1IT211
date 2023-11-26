from django.contrib import admin
from .models import MyUser

# Register your models here.

# admin.site.register(MyUser)

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'date_of_birth', 'role' )
    ordering=('first_name', 'last_name')