from django import forms
from .models import Reg
from django import forms

class RegForm(forms.Form):
    fname=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter First Name'

            }
        )
    )
    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name'

            }
        )
    )
    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Name'

            }
        )
    )
    pwd = forms.CharField(
        widget=forms.passwordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Password'

            }
        )
    )
    mobile = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Mobile Number'

            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email'

            }
        )
    )
    dob = forms.CharField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Date Of Birth'

            }
        )
    )
    gender = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Gender'

            }
        )
    )
    class RegForm(forms.ModelForm):
        class Meta:
            model=Reg
            fields=['fname','lname','user','pwd','mobile','email','dob','gender']

    class LoginForm(forms.Form):
        user=forms.CharField(max_length=20)
        pwd=forms.CharField(widget=forms.PasswordInput())