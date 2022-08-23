
from telnetlib import STATUS
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User, Task




GEEKS_CHOICES =(
    ("Pending", "Pending"),
    ("In Progress", "In Progress"),
    ("Completed", "Completed"),
    ("Cancelled", "Cancelled")
    
)

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'username',
            }

        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':'password',
            }   
        )
    )

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }

        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }   
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }   
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',

            }   
        )
    )
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email','is_admin','is_client','is_writter']



class AddTasks(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'title',
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder':'description',
            }
        )
    )
    file = forms.FileField(required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder':'file',
            }
        )
    )
    client_amount = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder':'client_amount',
            }
        )
    )
    # admin_amount = forms.IntegerField(
    #     widget=forms.NumberInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder':'admin_amount',
    #         }
    #     )
    # )
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder':'due_date',
            }
        )
    )
 

    class Meta:
        model = Task
        fields = ['title', 'description', 'file', 'client_amount','due_date']

class WritterForm(forms.Form):
       status = forms.ChoiceField(
        choices=GEEKS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder':'status',
            }
        )
    )
       file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder':'file',
            }
        )
    )

       class Meta:
            model = Task
            fields = ['status', 'file']
    