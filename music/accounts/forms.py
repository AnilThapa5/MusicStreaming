from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'username',
            'password',
            'email'
        }


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []


class ContactForm(forms.Form):
    name = forms.CharField(max_length=500, label="Name")
    email = forms.EmailField(max_length=500, label="Email")
    comment = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Enter your comment here'}))
