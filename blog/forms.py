from django.forms import ModelForm
from django import forms
from .models import Essays

# create Model Forms


class EssayForm(ModelForm):
    '''This form is for creating and changing and developing essay .'''
    class Meta:
        model = Essays
        fields = ('__all__')

        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }
