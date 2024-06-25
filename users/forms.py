from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'UsernameForm',
                                                             'placeholder': 'Enter your username'}))
    password = forms.CharField(label='Пароль', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'id': 'PasswordField',
                                                                 'placeholder': 'Enter your password'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class SignUpUserLogin(UserCreationForm):
    username = forms.CharField(label='Username', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'UsernameForm',
                                                             'placeholder': 'Enter your username'}))
    email = forms.EmailField(label='E-mail', required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'id': 'EmailForm',
                                                            'placeholder': 'Enter your email'}))
    password1 = forms.CharField(label='Пароль', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'id': 'PasswordField',
                                                                  'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label='Подтвердите пароль', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'id': 'ConfirmPasswordField',
                                                                  'placeholder': 'Confirm your password'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
    def cleaned_password2(self):
        cd = self.cleaned_data
        if cd['password1'] == cd['password2']:
            raise forms.ValidationError('Passwords don\'t match!')
        return cd['password1']

    def clean_email(self):
        cd = self.cleaned_data
        if get_user_model().objects.filter(email=cd['email']).exists():
            raise forms.ValidationError('E-mail уже зарегистрирован в системе!')
        return cd['email']
