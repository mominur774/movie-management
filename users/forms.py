from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': True})

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
