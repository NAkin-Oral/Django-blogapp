from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile

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

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100,widget = forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=100,widget = forms.TextInput(attrs={"class": "form-control"}))
    # last_login = forms.CharField(max_length=100,widget = forms.TextInput(attrs={"class": "form-control"}))
    # is_superuser = forms.CharField(max_length=100,widget = forms.CheckboxInput(attrs={"class": "form-check"}))
    # is_staff = forms.CharField(max_length=100,widget = forms.CheckboxInput(attrs={"class": "form-check"}))
    is_active = forms.CharField(max_length=100,widget = forms.CheckboxInput(attrs={"class": "form-check"}))
    # date_joined = forms.CharField(max_length=100,widget = forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email", "is_active")


class PasswordChanginForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs={"class": "form-control", "type":"password", "placeholder": "Enter your current password..."}))
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs={"class": "form-control", "type":"password","placeholder": "Enter your new password..."}))
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs={"class": "form-control", "type":"password","placeholder": "Re-enter your new password..."}))

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")

class EditProfilePage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_pic", "website_url","facebook_url", "instagram_url", "twitter_url"]
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control"}),
            "website_url": forms.TextInput(attrs={"class": "form-control"}),
            "facebook_url": forms.TextInput(attrs={"class": "form-control"}),
            "instagram_url": forms.TextInput(attrs={"class": "form-control"}),
            "twitter_url": forms.TextInput(attrs={"class": "form-control"}),
        }

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_pic", "website_url","facebook_url", "instagram_url", "twitter_url")
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control"}),
            # "profile_pic": forms.Textarea(attrs={"class": "form-control"}),
            "website_url": forms.TextInput(attrs={"class": "form-control"}),
            "facebook_url": forms.TextInput(attrs={"class": "form-control"}),
            "instagram_url": forms.TextInput(attrs={"class": "form-control"}),
            "twitter_url": forms.TextInput(attrs={"class": "form-control"}),
        }