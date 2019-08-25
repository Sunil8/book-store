from django import forms
from django.contrib import messages

class loginForm(forms.Form):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
        }))
    password=forms.CharField(label='password',widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'password'
        }))
class dashForm(forms.Form):
    book_name=forms.CharField(label='book_name')
    author_name=forms.CharField(label='author_name')
    published_date=forms.DateField(label='published_date')
    publisher=forms.CharField(label='publisher')
    Category=forms.CharField(label='Category')
    book_description=forms.CharField(label='book_description')
    book_image=forms.ImageField(label='book_image')


