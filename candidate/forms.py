from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CandidateRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    profession_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'profession_name']

class CandidateLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user and hasattr(user, 'candidateauth'):
                return self.cleaned_data
            else:
                raise forms.ValidationError("Invalid username or password.")
        raise forms.ValidationError("Both fields are required.")