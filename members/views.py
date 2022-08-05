from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from members.forms import RegistrationForm, BidderRegistrationForm
from django.http import HttpResponse
from members.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy, reverse
from IABC_WEB.models import Members



def home(request):
    type_obj=request.user
    if request.user.is_authenticated and type_obj.is_admin:
        return redirect('IABC_WEB:admember')
    elif request.user.is_authenticated and type_obj.is_bidder:
        return redirect('IABC_WEB:bidder_app')
    elif request.user.is_authenticated and type_obj.is_nonmember:
        info = User.objects.get(pk=request.user.id)
        return render(request, 'index.html', {'info':info})
    elif request.user.is_authenticated and type_obj.is_member:
        info = User.objects.get(pk=request.user.id)
        mem = Members.objects.get(user_id=request.user.id)
        context = {
            'mem':mem,
            'info':info 
        }
        return render(request, 'index.html', context)
    elif request.user.is_authenticated and type_obj.is_pending:
        info = User.objects.get(pk=request.user.id)
        return render(request, 'index.html', {'info':info})
    else:
        return render(request, 'index.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('members:home')
    else:
        if request.method == "POST":
            username = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                type_obj = request.user
                if user.is_authenticated:
                    return redirect('members:home')
                else:
                    messages.success(request, "Try Again")
                    return redirect('members:login') 
            else:
                messages.success(request, "Wrong Credentials")
                return redirect('members:login')
        else:
            return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('members:login')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url= reverse_lazy('members:home')



def register_view(request, *args, **kwargs):
    user = request.user
    context= {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination= kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("members:home")
        else:
            context['registration_form'] = form   

    return render(request, 'user-registration.html', context)


def bidder_register_view(request, *args, **kwargs):
    user = request.user
    context= {}

    if request.POST:
        form = BidderRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfuly Created!")
            return redirect("members:home")
        else:
            context['registration_form'] = form   

    return render(request, 'admin-registration.html', context)





