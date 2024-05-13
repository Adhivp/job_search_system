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
from company.views import *
from candidate.views import *
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register_company/', register_company, name='register_company'),
    path('company_login/', company_login, name='company_login'),
    path('company_login/', company_login, name='company_login'),
    path('company_dashboard',company_dashboard,name = 'company_dashboard'),
    path('register_candidate/', register_candidate, name='register_candidate'),
    path('edit_job_opening/<int:job_id>/',edit_job_opening, name='edit_job_opening'),
    path('delete_job_opening/<int:job_id>/',delete_job_opening, name='delete_job_opening'),
    path('candidate_login/', candidate_login, name='candidate_login'),
    path('job_listing_page/', job_listing_page, name='job_listing_page'),
    path('api/job-openings/', JobOpeningList.as_view(), name='job-opening-list')
]
