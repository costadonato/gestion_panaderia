from django import forms

from apps.producto.models import Producto


class NuevoProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'unidadMedida', 'precio', 'cantidad', 'tipo', 'cantidadMinima']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control input-sm', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values(): #esto es para cuestión de estilos
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'

class ModificarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'unidadMedida', 'precio', 'cantidad', 'tipo', 'cantidadMinima']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control input-sm', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values(): #esto es para cuestión de estilos
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'