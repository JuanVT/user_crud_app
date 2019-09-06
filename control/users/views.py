from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from control.users.forms import SignUpForm, EditProfileForm
from control.users.models import BaseUser


def signup(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
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
    return render(request, 'registration/edit_profile.html', context)
