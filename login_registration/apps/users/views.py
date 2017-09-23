from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    if 'id' in request.session:
        return redirect('/success')
    return render(request, ('users/index.html'))

def register(request):
    results = User.objects.basic_validator(request.POST)
    if results[0]:
        request.session['id'] = results[1].id
        request.session['register'] = True
        request.session['login'] = False
        print request.session['id']
        return redirect('/success')
    else:
        for tag, error in results[1].iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

def success(request):
    if 'id' not in request.session:
        return redirect('/')
    id = request.session['id']
    if request.session['register']:
        status = "registered"
    elif request.session['login']:
        status = "logged in"
    return render(request, ('users/success.html'), {'user': User.objects.get(id=id), 'status': status})

def login(request):
    results = User.objects.login_validator(request.POST)
    if results[0]:
        request.session['id'] = results[1].id
        request.session['login'] = True
        request.session['register'] = False
        return redirect('/success')
    else:
        for tag, error in results[1].iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')