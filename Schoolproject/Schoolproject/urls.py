"""Schoolproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from SchoolApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.base_view_page1),
    url(r'^Home/',views.base_page),
    url(r'^Pre Primary/',views.preprimary_view_page),
    url(r'^Primary/',views.primary_page),
    url(r'^High School/',views.highschool_page_view),
    url(r'^Enquiry/',views.enquiry_view_page),
    url(r'^Process/',views.process_view_page),
    url(r'^Founder/',views.founder_view_page),
    url(r'^Who we are/',views.whoweare_view_page),
    url(r'^Location/',views.Location_view_page),
    url(r'^Gallery/',views.Gallery_view_page),
    url(r'^Contact Us/',views.ContactUs_view_page),
    url(r'^Register Now/',views.Register_view_page)







]