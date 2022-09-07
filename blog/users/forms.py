from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from startblog.models import User
from django import forms

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["bio", "profile_picture", "website_url", "facebook_url", "twitter_url", "instagram_url", "pinterest_url" ]

        widgets = {
                "bio": forms.Textarea(attrs={"class": "form-control"}),
                # "profile_picture": forms.TextInput(attrs={"class": "form-control"}),
                "website_url": forms.TextInput(attrs={"class": "form-control"}),
                "facebook_url": forms.TextInput(attrs={"class": "form-control"}),
                "twitter_url": forms.TextInput(attrs={"class": "form-control"}),
                "instagram_url": forms.TextInput(attrs={"class": "form-control"}),
                "pinterest_url": forms.TextInput(attrs={"class": "form-control"}),

            }


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
          
          
        ]


class PasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}))
    new_password1 = forms.CharField(
        max_length=150, widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"})
    )
    new_password2 = forms.CharField(
        max_length=150, widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"})
    )

    class Meta:
        model = User
        fields = [
            "old_password",
            "new_password1",
            "new_password2",
        ]
