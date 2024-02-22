from django.contrib import auth
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import*
# Create your views here.
import random, string


def hello(request):
    return render(request, 'hello123.html')


def hello1(request):
    return HttpResponse("<center><font color='blue'>Welcome to TTM Homepage</font color></center>")


def newhomepage(request):
    return render(request, 'newhomepage.html')


def Travel(request):
    return render(request, 'TravelPackage.html')


def print1(request):
    return render(request, 'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input:{user_input}')
    # return HttpResponse('Form submitted successfully')
    a1 = {'user_input': user_input}
    return render(request, 'print_to_console.html', a1)


def randomotp(request):
    return render(request, "Randomotp.html")


def randomotp1(request):
    if request.method == "POST":
        input1 = request.POST['otp']
        input2 = int(input1)
        result_str = ''.join(random.sample(string.digits, input2))
        print(result_str)
        context = {'result_str': result_str}
        return render(request, "Randomotp.html", context)


def randomexample(request):
    ran1 = ''.join(random.sample(string.digits, k=6))
    print(ran1)
    a2 = {'ran1': ran1}
    return render(request, 'randomexample.html', a2)


def getdate(request):
    return render(request, 'getdate1.html')


import datetime
from django.shortcuts import render
from .forms import *


def getdate1(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'getdate1.html', {'updated_date': updated_date})
        else:
            form = IntegerDateForm()
            return render(request, 'getdate1.html', {'form': form})


def tzfunctioncall(request):
    return render(request, 'pytzexample.html')
##def tzfunctionlogic(request):
    ##return
def registercallfunction(request):
    return render(request,'myregisterpage.html')

from django.shortcuts import render, redirect
def registerloginfunction(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password =  request.POST.get('password')
    phonenumber =  request.POST.get('phonenumber')
    #check if the email already exists
    if Register.objects.filter(email =  email).exists():
        message1 = "Email already registered.Choose a different email."
        # return HttpResponse("Email already registered.Choose a different email.")
        return render(request,'myregisterpage.html',{'message1':message1})
        #create a new Register instance and save it
        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('newhomepage')
        return render(request, 'myregisterpage.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})

class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')

def places(request):
    return render(request, 'places.html')


from django.contrib import messages

def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def signup1(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
                 if User.objects.filter(username=username).exists():
                     messages.info(request,'OOPS! Username already taken')
                     return render(request,'signup.html')
                 else:
                     user=User.objects.create_user(username=username,password=pass1)
                     user.save()
                     messages.info(request,'Account created successfully!')
                     return render(request,'login.html')
        else:
                    messages.info(request, 'Password do not match')
                    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')

def contact(request):
    return render(request,'contact.html')

def contactmail(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment + '................This is just the'
        data = contactus(firstname=firstname, lastname=lastname, email=email, comment=comment)
        data.save()
        return HttpResponse("<h1><center> Thank you for giving your feedback</center></h1>")

