from django import forms
from django.forms import DateInput
from apps.empleado.models import Empleado


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['cuit', 'nombre_completo', 'telefono', 'fecha_nacimiento', 'fecha_incorporacion', 'domicilio_calle',
                  'domicilio_numero', 'domicilio_localidad', 'domicilio_departamento', 'usuario']
        widgets = {
            'fecha_nacimiento': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_incorporacion': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values(): #esto es para cuestión de estilos
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'