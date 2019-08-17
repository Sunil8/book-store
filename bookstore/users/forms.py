from django import forms
# from django.contrib import admin
# from django.contrib.auth.models import Group
from users.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    """A from for creating new users."""
    password1 = forms.CharField(
        label = 'Password', 
        widget = forms.PasswordInput
    )
    password2 = forms.CharField(
        label = 'Confirm Password', 
        widget = forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password1 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords dont' match")

        return password2

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """ A from for updating users."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            # 'avatar',
            'password', 
            'is_active',
        )

    def clean_password(self):
        return self.initial["password"]
