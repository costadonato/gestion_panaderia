

from django import forms
from django.forms import inlineformset_factory

from apps.pedido.models import MateriaPrima, Pedido, ItemPedido


class NuevaMateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = MateriaPrima
        fields = ['nombre', 'cant_disponible', 'proveedor']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ModificarMateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = MateriaPrima
        fields = ['nombre', 'cant_disponible', 'proveedor']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class NuevoPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['proveedor','observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'class': 'form-control input-sm', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values(): #esto es para cuestión de estilos
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'



class NuevoItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['materia_prima', 'precio_unid', 'cantidad']

    def _init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():  # esto es para cuestión de estilos
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'


# Crear el formset para los items
ItemPedidoFormSet = inlineformset_factory(
    Pedido,
    ItemPedido,
    form=NuevoItemPedidoForm,
    extra=1,  # Número de formularios vacíos
    can_delete=True  # Permite eliminar secciones
)