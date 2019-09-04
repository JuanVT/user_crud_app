from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader


@login_required()
def index(request):
    context = {}

    template = loader.get_template('control/index.html')
    return HttpResponse(template.render(context=context, request=request))


def login(request):
    context = {}

    template = loader.get_template('users/user_login.html')
    return HttpResponse(template.render(context=context, request=request))
