from django import forms

from accounts.constants import USER_TYPE_CHOICES, YES_NO
from accounts.models import Account


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=50, disabled=True)
    email = forms.EmailField(disabled=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'email')

        def clean_password2(self):
            # Check that the two password entries match
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            return password2