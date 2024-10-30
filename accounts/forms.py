# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm,PasswordChangeForm,SetPasswordForm

from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username or Email', 'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password', 'autocomplete':'current_password','class': 'form-control'
    }))
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']  # Use 'username' and 'email'
        labels = {
            'username': 'Username',  # Label for the username field
            'email': 'Email Address',  # Label for the email field
        }
    

        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    # Override save method to hash the password before saving
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password
        if commit:
            user.save()
        return user
        
class MyPasswordChangeForm(PasswordChangeForm):
   
    old_password = forms.CharField(label="old password", widget=forms.PasswordInput(
        attrs={'autofocus':'True', 'auto_complete':'current_password','class':'form-controlo'}
    ))
    new_password1 = forms.CharField(label="new_password1", widget=forms.PasswordInput(
        attrs={'autofocus':'True', 'auto_complete':'current_password','class':'form-controlo'}
    ))
    new_password2 = forms.CharField(label="new_password2", widget=forms.PasswordInput(
        attrs={'autofocus':'True', 'auto_complete':'current_password','class':'form-controlo'}
    ))
class PasswordResetForm(PasswordResetForm):
       email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        }))
    
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter new password'
        }),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm new password'
        }),
        strip=False,
    )

# forms.py
from django import forms
from .models import Customer

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'mobile', 'city', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name', 'class': 'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'placeholder': 'Enter your mobile number', 'class': 'form-control'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Enter your city', 'class': 'form-control'
            }),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={
                'placeholder': 'Enter your zip code', 'class': 'form-control'
            }),
        }

class AddressForm(forms.ModelForm):
     class Meta:
        model = Customer
        fields = ['name', 'mobile', 'city', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name', 'class': 'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'placeholder': 'Enter your mobile number', 'class': 'form-control'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Enter your city', 'class': 'form-control'
            }),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={
                'placeholder': 'Enter your zip code', 'class': 'form-control'
            }),
        }

