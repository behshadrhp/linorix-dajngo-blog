from django.forms import Form
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ReCaptchaForm(Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)