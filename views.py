from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import userProfile
from django.contrib.auth.decorators import login_required
import os
from Product.models import Cart
from Product.models import*



# Create your views here.
def home(request):
    user=request.user.id
    cart_prod=Cart.objects.filter(user=user)
    cc = Cart.objects.filter(user=user).count()
    l=location.objects.all()
    c=Category.objects.all()
    cat_id=request.GET.get('cat_id')
    if request.method =='GET' :
        src=request.GET.get('search')

    if src:
        p=Product.objects.filter(name__icontains=src)
    elif cat_id:
        p=Product.objects.filter(category=cat_id)
    else:
        p=Product.objects.all()
    return render(request, 'home.html',locals())


def base(request):
    return render(request, 'base.html')


def login(request):
    us = request.user
    if us.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active & user.is_staff:
                    auth.login(request, user)
                    messages.success(request, 'Log In successful')
                    return redirect('profile')
                else:
                      auth.login(request, user)
                      messages.success(request, 'Log In successful')
                      return redirect('home')
            else:
                messages.error(request, 'User is Not Found!Please do Registration First.')
                return redirect('registration')


    return render(request, 'login.html')


def registration(request):
    us = request.user
    if us.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            first_name = request.POST['First_name']
            last_name = request.POST['Last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password1 = request.POST['password1']
            if password == password1:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username is already taken.')
                    return redirect(registration)
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'email is already taken.')
                    return redirect(registration)
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    email=email, password=password)
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'Registration Done!')
                    return redirect(login)
    return render(request, 'registration.html')


def logout(request):
    messages.success(request, 'Logged out')
    auth.logout(request)
    return redirect('login')


@login_required(login_url=login)
def Profile(request):
    delete = request.GET.get('profile')
    if delete:
        delete_user = User.objects.get(id=delete)
        delete_user.delete()
        return redirect('login')

    a = User.objects.get(id=1)
    user1 = userProfile.objects.get(user=a)
    if request.method == 'POST':
        phn = request.POST.get('phn')
        birth = request.POST.get('birth')
        add = request.POST.get('add')
        img = request.FILES.get('img')
        if len(request.FILES) != 0:
            if len(user1.image) > 0:
                if user1.image != 'default.jpg':
                    os.remove(user1.image.path)
            user1.image = img
        user1.phone_number = phn
        user1.birthday = birth
        user1.address = add
        user1.save()
        return redirect('profile')

    Context = {
        "user1": user1
    }

    return render(request, 'profile.html', Context)
