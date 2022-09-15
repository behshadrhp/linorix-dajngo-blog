from dataclasses import field
from django.forms import ModelForm
from django import forms
from .models import Essay, Comment

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


class CommentForm(ModelForm):
    '''This class is for commenting'''

    class Meta:
        model = Comment
        fields = ['value' , 'body']

        labels = {
            'body':'Add a comment with your vote',
            'comment':'place your vote'
        }


    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():

            field.widget.attrs.update(
                {
                    'class':'class="label-comment"'
                }
            )

        self.fields['value'].widget.attrs.update(
            {
                'class':'comment-vote'
            }
        )

        self.fields['body'].widget.attrs.update(
            {
                'placeholder':'writing comment ✍️',
            }
        )
