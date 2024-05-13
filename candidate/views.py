from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CandidateRegistrationForm,CandidateLoginForm
from .models import CandidateAuth

def register_candidate(request):
    if request.method == 'POST':
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            candidateAuth =CandidateAuth.objects.create(
                user=user,
                name=form.cleaned_data['name'],
                profession_name=form.cleaned_data['profession_name']
            )
            return redirect('candidate_login')  
    else:
        form = CandidateRegistrationForm()
    return render(request, 'register_candidate.html', {'form': form})

def candidate_login(request):
    if request.method == 'POST':
        form = CandidateLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('job_listing_page')
    else:
        form = CandidateLoginForm()
    return render(request, 'candidate_login.html', {'form': form})

def job_listing_page(request):
    return render(request,'job_listing_page.html')