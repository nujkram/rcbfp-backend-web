from django import forms
from django.contrib.auth.forms import AuthenticationForm

from accounts.constants import USER_CREATION_TYPE_CHOICES
from accounts.models import Account


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = (
            'email',
            'password',
        )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )


class LoginForm(AuthenticationForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = (
            'email',
            'password',
        )


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = (
            'user_type',
            'email',
            'password',
        )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['user_type'].choices = USER_CREATION_TYPE_CHOICES

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password doesn't match"
            )