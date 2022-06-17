from django import forms
from .models import KeyValueModel


class KeyvalueForm(forms.ModelForm):
    class Meta:
        model = KeyValueModel
        fields = ("key","value")
        widgets = {
            'key': forms.TextInput(attrs={"placeholder":"key", "class":"textinp"}),
            'value': forms.TextInput(attrs={"placeholder":"value", "class":"textinp"}),
        }
