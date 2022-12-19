from django import forms
from test3y4.models import Seminario

class FormSeminario(forms.ModelForm):
    class Meta:
        model = Seminario
        fields = '__all__'