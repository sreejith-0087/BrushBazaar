from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import CustomerDetails
from django.contrib.auth.decorators import login_required

# Create your views here.

def Register(request):
    if request.method == 'POST':
        first_name = request.POST.get('c_fname')
        last_name = request.POST.get('c_lname')
        email = request.POST.get('c_email')
        phone = request.POST.get('c_phone')
        password = request.POST.get('c_password')
        repassword = request.POST.get('c_repassword')
        address = request.POST.get('c_addr')
        photo = request.FILES.get('c_photo')

        if password != repassword:
            messages.error(request, 'Password do not match!')
            return redirect('Customer:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('Customer:register')

        if not phone.isdigit() or len(phone) !=10:
            messages.error(request, 'Phone number must be 10 digits')
            return redirect('Customer:register')

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()

            customer = CustomerDetails(
                id=user,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                address=address,
                photo=photo
            )
            customer.save()

            messages.success(request, 'Registration successful')
            return redirect('Customer:login')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('Customer:register')

    return render(request, 'Customer/Register.html')


def Login(request):
    if request.method == 'POST':
        email = request.POST['c_email']
        password = request.POST['c_password']
        user = auth.authenticate(username=email, password=password)

        if user is not None and CustomerDetails.objects.filter(id=user.id).exists():
            auth.login(request, user)
            return redirect('Shop:home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'Customer/Login.html')


def Logout(request):
    auth.logout(request)
    messages.error(request, 'Logout Successful')
    return redirect('Customer:login')