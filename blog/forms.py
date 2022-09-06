from django.forms import ModelForm
from django import forms
from .models import Essay

# create Model Forms


class EssayForm(ModelForm):
    '''This form is for creating and changing and developing essay .'''
    class Meta:
        model = Essay
        fields = ['title', 'upload_image', 'description',
                  'source_link', 'demo_link', 'total_vote', 'positive_vote', 'tag']

        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
            'upload_image': forms.FileInput(),
        }
