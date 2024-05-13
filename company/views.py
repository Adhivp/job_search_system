from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .forms import CompanyLoginForm
from .forms import CompanyRegistrationForm
from .models import CompanyAuth
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import JobOpening
from .serializers import JobOpeningSerializer

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

@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_job_opening(request):
    if request.method == 'POST':
        user = request.user
        
        try:
            company_auth = user.companyauth
        except CompanyAuth.DoesNotExist:
            return Response({'error': 'Company profile does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        
        serializer = JobOpeningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_job_opening(request, pk):
    
    try:
        job_opening = JobOpening.objects.get(pk=pk)
    except JobOpening.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        job_opening.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def company_dashboard(request):
    return render(request,'company_dashboard.html')
