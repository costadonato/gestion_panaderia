from django import forms

from apps.proveedor.models import Proveedor

class NuevoProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'email', 'domicilioCalle', 'domicilioNum', 'domicilioLocalidad', 'domicilioDepartamento', 'razonSocial' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ModificarProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'email', 'domicilioCalle', 'domicilioNum', 'domicilioLocalidad', 'domicilioDepartamento', 'razonSocial' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'