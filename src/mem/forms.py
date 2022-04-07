from django import forms
from django.contrib.auth.forms import UserCreationForm



class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")
