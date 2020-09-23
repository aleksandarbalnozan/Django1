from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# This class will overwrite origginal UserCreationForm0
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        # this will add email to our register_form
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('User with same email already exists')
        return email

        # THIS VALIDATION WORKS TOO
    # def clean_email(self):
    #    email = self.cleaned_data['email']
    #    if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email exists")
    #    return self.cleaned_data
