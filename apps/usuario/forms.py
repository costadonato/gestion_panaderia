from django.contrib.auth.forms import UserCreationForm

from apps.usuario.models import Usuario


class UsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields+ ('cuit',) #campos que se quieren en el formulario