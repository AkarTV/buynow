from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    #add_form = UserCreationForm   
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Персональная информация'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'avatar')}),
        (('Права доступа'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Важные даты'), {'fields': ('last_login', 'date_joined')}),
    )

'''
class CustomUserAdmin(UserAdmin):
    ...
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'avatar',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'avatar',)}),
    )  
'''
admin.site.register(User, CustomUserAdmin)