from django.contrib.auth import login
from django.shortcuts import redirect, render

from control.users.forms import SignUpForm


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
