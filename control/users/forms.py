from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm
)

from control.users.models import BaseUser


class SignUpForm(UserCreationForm):
    email1 = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='Email Confirmation')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = BaseUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email1',
            'email2'
        )

    def clean(self):
        super().clean()
        email1 = self.cleaned_data.get('email1')
        email2 = self.cleaned_data.get('email2')

        if email1 != email2:
            raise forms.ValidationError(
                'Email addresses must match!'
            )

        email_qs = BaseUser.objects.filter(email=email1)

        if email_qs.exists():
            raise forms.ValidationError(
                'Email address already exists!'
            )


class EditProfileForm(UserChangeForm):
    phone_number = forms.DecimalField(label='Phone Number', required=False)
    Address = forms.CharField(label='Address', required=False)
    company = forms.CharField(label='Company', required=False)
    job_title = forms.CharField(label='Job Title', required=False)
    location = forms.CharField(label='Location', required=False)
    bio = forms.CharField(label='Bio', required=False)
    password = None

    class Meta:
        model = BaseUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'address',
            'phone_number',
            'company',
            'job_title',
            'location',
            'bio'
        )


class ResetPasswordForm(PasswordChangeForm):
    class Meta:
        model = BaseUser
        fields = (
            'old_password',
            'new_password1',
            'new_password2'
        )
