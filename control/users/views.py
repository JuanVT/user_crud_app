from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from control.users.forms import (
    SignUpForm,
    EditProfileForm,
    ResetPasswordForm
)
from control.users.models import BaseUser


def signup(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email1')

            user.set_password(password)
            user.email = email
            user.save()

            login(
                request,
                user,
                backend='django.contrib.auth.backends.ModelBackend'
            )
            return redirect('/')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)


@login_required()
def view_profile(request):
    user = request.user

    context = {
        'user': user
    }
    return render(request, 'users/profile.html', context)


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'users/edit_profile.html', context)


@login_required()
def password_reset(request):
    if request.method == 'POST':
        form = ResetPasswordForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
    else:
        form = ResetPasswordForm(request.user)

    context = {
        'form': form,
    }
    return render(request, 'registration/password_reset.html', context)


@login_required()
def delete_confirmation(request):  # User's account deletion
    return render(request, 'registration/delete_confirmation.html')


@login_required()
def account_deletion(request, user_id):
    user = BaseUser.objects.get(id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('/')
