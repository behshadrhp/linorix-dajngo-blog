from django.forms import ModelForm
from django import forms
from .models import Essay

# create Model Forms


class EssayForm(ModelForm):
    '''This form is for creating and changing and developing essay .'''
    class Meta:
        model = Essay
        fields = ('__all__')

        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }
