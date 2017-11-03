from django import forms
from .models import Pick


class CreatePickForm(forms.ModelForm):

    class Meta:
        model = Pick
        fields = ('prediction', 'category')

        widgets = {
            'prediction': forms.TextInput(),
        }
