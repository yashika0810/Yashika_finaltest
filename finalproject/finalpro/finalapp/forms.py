from django import forms
from . models import fullname


class Userproform(forms.ModelForm):
    class Meta:
        model=fullname
        fields="__all__"
