from django.shortcuts import render,redirect
from product.models import Product
from .forms import RegistrationForm
from .models import Account
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():

            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            mobile=form.cleaned_data['mobile']
            password=form.cleaned_data['password']
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,mobile=mobile,password=password)
            user.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect('register')
    else:

        form=RegistrationForm()

        #print('Not Registered')

    context={'form':form}

    return render(request, 'register.html',context)

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Login successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid User.')
            return redirect('signin')


    return render(request, 'signin.html')
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,'Logout successfully..')
    return redirect('signin')
