from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegestrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "password1", "password2"]


class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SendMoneyForm(forms.Form):
    receiver_card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    