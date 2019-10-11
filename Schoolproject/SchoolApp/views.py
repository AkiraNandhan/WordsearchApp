from django.shortcuts import render


def base_view_page1(request):
    return render(request,'base1.html')


def base_page(request):
    return render(request,'home.html')


def preprimary_view_page(request):
    return render(request,'preprimary.html')


def primary_page(request):
    return render(request,'primary.html')


def highschool_page_view(request):
    return render(request,'highschool.html')


def enquiry_view_page(request):
    return render(request,'enquiry.html')


def process_view_page(request):
    return render(request,'process.html')


def founder_view_page(request):
    return render(request,'Founder.html')


def whoweare_view_page(request):
    return render(request,'whoweare.html')


def Location_view_page(request):
    return render(request,'location.html')


def Gallery_view_page(request):
    return render(request,'gallery.html')


def ContactUs_view_page(request):
    return render(request,'contactus.html')


def Register_view_page(request):
    return render(request,'Register.html')