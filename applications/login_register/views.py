from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
# Create your views here.

def sessionLogIn(request):
    if request.method == "GET":
        return render(request, 'login_&_register/login.html')
    elif request.method == "POST":
        if not request.POST['username'] and not request.POST['password'] :
            return render(request, 'login_&_register/login.html',{
                    "error": 'No se han completado todos los datos.'
                })
        else :
            user = authenticate(request, username = request.POST['username'] , password = request.POST['password'])
            if user is None :
                return render(request, 'login_&_register/login.html',{
                    "error": 'Los datos ingresados son incorrectos.'
                })
            else:
                login(request, user)
                return redirect('http://127.0.0.1:8080/')

def sessionRegister(request):
    if request.method == "GET":
        return render(request, 'login_&_register/register.html')
    elif request.method == "POST":
        if not request.POST['email'] and not request.POST['password'] and not request.POST['username']:
            return render(request, 'login_&_register/register.html',{
                    "error": 'No se han completado todos los datos.'
                })
        else :
            try:
                user = User.objects.create_user(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password']
                    )
                user.save()
                login(request, user)
                return redirect('http://127.0.0.1:8080/')
            except IntegrityError:
                return render(request, 'login_&_register/register.html',{
                    "error": '¡El usuario ingresado ya existe!'
                })

def sessionLogOut(request) :
    logout(request)
    return redirect('http://127.0.0.1:8080/')