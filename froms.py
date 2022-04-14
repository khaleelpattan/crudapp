from django import forms

from .models import hello


class helloform(forms.ModelForm):

    class Meta:

        model = hello

        fields = "__all__"
