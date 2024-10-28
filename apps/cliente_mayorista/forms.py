from django import forms

from apps.cliente_mayorista.models import ClienteMayorista


class NuevoClienteMayoristaForm(forms.ModelForm):
    class Meta:
        model = ClienteMayorista
        fields = ['nombre_completo', 'cuit','telefono','email', 'domicilio_calle', 'domicilio_numero', 'domicilio_localidad',
                  'domicilio_departamento']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values(): #esto es para cuestión de estilos
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'





class ModificarClienteMayoristaForm(forms.ModelForm):
    class Meta:
        model = ClienteMayorista
        fields = ['nombre_completo', 'telefono','email', 'domicilio_calle', 'domicilio_numero', 'domicilio_localidad',
                  'domicilio_departamento']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'