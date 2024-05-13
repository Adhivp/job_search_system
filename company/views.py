from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CompanyLoginForm
from .forms import CompanyRegistrationForm
from .models import CompanyAuth

def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            company_auth = CompanyAuth.objects.create(
                user=user,
                company_name=form.cleaned_data['company_name'],
                bio=form.cleaned_data['bio']
            )

            return redirect('company_login') 
    else:
        form = CompanyRegistrationForm()
    return render(request, 'register_company.html', {'form': form})

def company_login(request):
    if request.method == 'POST':
        form = CompanyLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None and hasattr(user, 'companyauth'):
                login(request, user)
                return redirect('company_dashboard')
    else:
        form = CompanyLoginForm()
    return render(request, 'company_login.html', {'form': form})

def company_dashboard(request):
    return render(request,'company_dashboard.html')
