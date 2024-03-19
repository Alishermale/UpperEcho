from django import forms
from .models import TextData


class TextDataForm(forms.ModelForm):
    class Meta:
        model = TextData
        fields = ['text']
