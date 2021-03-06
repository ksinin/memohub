from django import forms
from django.contrib.auth.forms import UserCreationForm

from mem.models import Mem


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-input'})
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")


class MemAddForm(forms.ModelForm):
    class Meta:
        model = Mem
        fields = ["url", "description"]
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-input', 'label': 'URL'}),
            'description': forms.Textarea(
                attrs={'cols': 30, 'rows': 10, 'class': 'form-input', 'label': 'Description'}
            ),
        }
