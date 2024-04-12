from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from input_valid.logic import Check_Yaml


# Create your views here.
@csrf_exempt
def main(request):
    return HttpResponse("Welcome to the home page")

@csrf_exempt
def host(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a host: {user_input} ", Check_Yaml.hostInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_host.html')

def state(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a state: {user_input} ", Check_Yaml.stateInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_state.html')

def namesubject(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a name/subject: {user_input} ", Check_Yaml.nameSubjectInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_namesubject.html')

def port(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a port: {user_input} ", Check_Yaml.portInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_port.html')

def email(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered an email: {user_input} ", Check_Yaml.emailInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_email.html')

def bodymsg(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a body/message: {user_input} ", Check_Yaml.bodyMsgInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_bodymsg.html')

def command(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a command: {user_input} ", Check_Yaml.commandInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_command.html')

def count(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a count: {user_input} ", Check_Yaml.countInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_count.html')

def unit(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a unit: {user_input} ", Check_Yaml.unitInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_unit.html')

def timespec(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a timespec: {user_input} ", Check_Yaml.timespecInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_timespec.html')

def repo(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a repo: {user_input} ", Check_Yaml.repoInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_repo.html')

def dest(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            return HttpResponse(f"You successfully entered a destination: {user_input} ", Check_Yaml.destInput(user_input))
        except ValueError:
            return HttpResponse(f"Value error detected")
    else:
        return render(request, 'input_form_dest.html')

def second_in(request):
    return HttpResponse("Welcome to the second page")
