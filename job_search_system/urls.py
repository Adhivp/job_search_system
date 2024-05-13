"""
URL configuration for job_search_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from company.views import register_company,company_login,company_dashboard
from candidate.views import register_candidate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_company/', register_company, name='register_company'),
    path('register_candidate/', register_candidate, name='register_candidate'),
    path('company_login/', company_login, name='company_login'),
    path('company_login/', company_login, name='company_login'),
    path('company_dashboard',company_dashboard,name = 'company_dashboard')
    
]
