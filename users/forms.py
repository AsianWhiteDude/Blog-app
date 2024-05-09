from django import forms


class LoginUserForm(forms.Form):
    email = forms.EmailField(label='Your Email...', required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'id': 'EmailForm'}))
    password = forms.CharField(label='Enter Password...', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'id': 'PasswordField'}))
