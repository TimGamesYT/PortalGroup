from django import forms
from .models import Material

class CreateMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['description', 'media']

        labels = {
            'description': 'Опис',
            'media': 'Медіа'
        }