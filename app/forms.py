from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'Placeholder' : 'First name','class':'form-control',
                                                               }))

    last_name = forms.CharField(max_length=100,
                                    required=True,
                                    widget=forms.TextInput(attrs={'Placeholder' : 'Last name','class':'form-control',
                                                                }))
    Username = forms.CharField(max_length=100,
                                    required=True,
                                    widget=forms.TextInput(attrs={'Placeholder' : 'Username','class':'form-control',
                                                                }))
    email = forms.EmailField(required=True,
                                widget=forms.TextInput(attrs={'Placeholder' : 'Email','class':'form-control',
                                                        }))
    password = forms.CharField(max_length=50,
                                    required=True,
                                    widget=forms.TextInput(attrs={'Placeholder' : 'Password','class':'form-control',
                                                                'data-toggle':'password',
                                                                'id':'password',
                                                                }))
    password2 = forms.CharField(max_length=50,
                                    required=True,
                                    widget=forms.TextInput(attrs={'Placeholder' : 'Confirm Password','class':'form-control',
                                                                'data-toggle':'password',
                                                                'id':'password',
                                                                }))
class Meta:
    model = User
    fields =['first_name','last_name','username','email','password','password2']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('food',)
    