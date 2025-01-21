from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from .models import CustomerDetails, Feedback
from django.contrib.auth.decorators import login_required
from Shop.models import BrushBazaarProducts
from . forms import CustomPasswordChangeForm, CustomerDetailsForm

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


@login_required(login_url='Customer:login')
def Addfeedback(request, pro_id):
    if request.method == 'POST':
        fed = request.POST['Add_Feedback']
        product = BrushBazaarProducts.objects.get(id=pro_id)
        user = CustomerDetails.objects.get(id=request.user.id)
        Feedback(user=user, feedback=fed, product=product).save()
        return redirect('Shop:single_product', pro_id)


def Product_Feedback_View(request, product_id):
    feedback_list = Feedback.objects.filter(product_id=product_id).order_by('-created_at')
    return render(request, 'Shop:single_product', {'feedback_list': feedback_list})



@login_required(login_url='Customer:login')
def Profile(request):
    customer = get_object_or_404(CustomerDetails, id=request.user)
    if request.method == "POST":
        form = CustomerDetailsForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('Customer:profile')
        else:
            messages.error(request, "Error updating profile. Please correct the highlighted fields.")
    else:
        form = CustomerDetailsForm(instance=customer)
    return render(request, 'Customer/Profile.html', {'form': form})


@login_required(login_url='Customer:login')
def Change_Password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Your password was successfully updated!")
            return redirect('Customer:profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'Customer/Change_Password.html', {'form': form})