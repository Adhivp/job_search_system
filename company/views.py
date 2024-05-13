from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import CompanyLoginForm,CompanyRegistrationForm,JobOpeningForm
from .models import CompanyAuth
from .models import JobOpening

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
    if request.method == 'POST':
        form = JobOpeningForm(request.POST)
        if form.is_valid():
            job_opening = form.save(commit=False)
            job_opening.company = request.user.companyauth
            job_opening.save()
            return redirect('company_dashboard')
    else:
        form = JobOpeningForm()
    job_openings = JobOpening.objects.filter(company=request.user.companyauth)
    return render(request, 'company_dashboard.html', {'form': form, 'job_openings': job_openings})

def edit_job_opening(request, job_id):
    job_opening = get_object_or_404(JobOpening, pk=job_id)
    if request.method == 'POST':
        form = JobOpeningForm(request.POST, instance=job_opening)
        if form.is_valid():
            form.save()
            return redirect('company_dashboard')
    else:
        form = JobOpeningForm(instance=job_opening)
    return render(request, 'edit_job_opening.html', {'form': form})

def delete_job_opening(request, job_id):
    job_opening = get_object_or_404(JobOpening, pk=job_id)
    if request.method == 'POST':
        job_opening.delete()
        return redirect('company_dashboard')
    return render(request, 'delete_job_opening.html', {'job_opening': job_opening})