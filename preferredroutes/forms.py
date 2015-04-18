from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from django import forms

class RouteWXForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RouteWXForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'dep',
            'arr',
            'alt',
            ButtonHolder(
                Submit('routewx', 'Get Routes', css_class='btn-primary')
            )
        )


    dep = forms.CharField(label='DEP', max_length=4)
    arr = forms.CharField(label='ARR', max_length=4)
    alt = forms.CharField(label='ALT', max_length=4)

