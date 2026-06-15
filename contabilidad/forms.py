from django import forms
from .models import Producto # Asegúrate de importar el modelo 'Producto'

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Producto # Aquí DEBE decir Producto, no NombreDeTuModelo
        fields = '__all__'

