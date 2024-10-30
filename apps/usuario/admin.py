from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.usuario.forms import UsuarioForm
from apps.usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cuit',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'cuit', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'cuit', 'username',)
