from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from control.settings import LOGIN_REDIRECT_URL
from control.users.forms import UserLoginForm


@login_required()
def index(request):
    context = {}

    template = loader.get_template('control/index.html')
    return HttpResponse(template.render(context=context, request=request))


def user_login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(LOGIN_REDIRECT_URL)
        return redirect('/')

    context = {
        'form': form
    }

    template = loader.get_template('users/user_login.html')
    return HttpResponse(template.render(context=context, request=request))
