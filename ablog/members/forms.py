from socket import fromshare
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email adress..."}))
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your first name..."}))
    last_name = forms.CharField(max_length=100,widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your last name..."}))

    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] ="form-control"
        self.fields["username"].widget.attrs["placeholder"] ="Enter your username..."
        self.fields["password1"].widget.attrs["class"] ="form-control"
        self.fields["password1"].widget.attrs["placeholder"] ="Enter your password..."
        self.fields["password2"].widget.attrs["class"] ="form-control"
        self.fields["password2"].widget.attrs["placeholder"] ="Re-enter your password..."
