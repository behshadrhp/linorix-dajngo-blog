from dataclasses import field
from django.forms import Form, ModelForm, FileInput
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill, Message
from user import models


class ReCaptchaForm(Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Full Name',
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Full Name',

            }
        )

        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'UserName',
                'minlength': '5',
                'title': 'Username must be more than 5 characters .',
            }
        )

        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Email',
                'pattern': "^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$",
                'title': 'Please enter a valid email',
            }
        )

        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Password',
                'id': 'pwd',
                'minlength': '8',
                'pattern': '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).*$',
                'title': 'Your number of characters must be more than 8 and a combination of at least 1 uppercase letter, 1 lowercase letter and 1 number.',
            }
        )

        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Config Password',
                'minlength': '8',
                'pattern': '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).*$',
                'title': 'Your number of characters must be more than 8 and a combination of at least 1 uppercase letter, 1 lowercase letter and 1 number.',
            }
        )


class UpdateInformationForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'avatar': FileInput(),
        }


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']


class MessageFormAnonymous(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
        labels = {
            'name':'Full Name',
        }

class MessageFormUser(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']
        labels = {
            'name':'Full Name',
        }