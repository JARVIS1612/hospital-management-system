from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'number', 'age', 'gender', 'blood_group', 'is_patient', 'is_doctor', 'is_pharma')

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': "Enter Username",
                    'class': "form-control"
                },
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter Firstname",
                    'class': "form-control"
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter Lastname",
                    'class': "form-control"

        }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': "Abc@gmail.com",
                    'class': "form-control"

                }
            ),
            'number': forms.TextInput(
                attrs={
                    'label': "Mobile Number",
                    'placeholder': "Enter Mobile Number",
                    'class': "form-control"

                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': "Enter Your Age",
                    'class': "form-control"

                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
            'blood_group': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'placeholder': "Enter Password",
                    'class': "form-control"
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder': "Conform your password",
                    'class': "form-control"
                }
            )
        }