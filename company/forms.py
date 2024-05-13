from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CompanyRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'company_name', 'bio']

class CompanyLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user and hasattr(user, 'companyauth'):
                return self.cleaned_data
            else:
                raise forms.ValidationError("Invalid username or password.")
        raise forms.ValidationError("Both fields are required.")