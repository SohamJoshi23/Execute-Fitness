from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import MembershipForm
from .models import Membership

def Home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def Trainers(request):
    template = loader.get_template('Trainers.html')
    return HttpResponse(template.render())

# def About(request):
#     template = loader.get_template('About.html')
#     return HttpResponse(template.render())

def about(request):
    return render(request, 'About.html')
# def about1(request):
#     return render(request, 'About.html')

def Bmical(request):
    template = loader.get_template('Bmical.html')
    return HttpResponse(template.render())

def bmi(request):
    template = loader.get_template('FinalBMI.html')
    return HttpResponse(template.render())

def Diet1(request):
    template = loader.get_template('Diet1.html')
    return HttpResponse(template.render())

def Gallery(request):
    template = loader.get_template('Gallery.html')
    return HttpResponse(template.render())

def FG(request):
    template = loader.get_template('FinalGallery.html')
    return HttpResponse(template.render())

def TF(request):
    template = loader.get_template('TrainersFinal.html')
    return HttpResponse(template.render())

def price(request):
    template = loader.get_template('pricing.html')
    return HttpResponse(template.render())

def  MembershipData(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        membership_type = request.POST.get('membership_type')
        add=Membership.objects.create(full_name=full_name,phone_number=phone_number,email=email,membership_type=membership_type)
        # Create a new Membership object and save it to the database
        # add=Membership.objects.create(
        #     full_name=full_name,
        #     phone_number=phone_number,
        #     email=email,
        #     membership_type=membership_type
        # )
        add.save()
        return redirect('Home')  # Redirect to home page after successful submission
    else:
        # If it's a GET request or form submission was unsuccessful, render a blank form
        return render(request, 'Member1.html')


    # return render(request,'Member1.html')
# def Membership(request):
#     template = loader.get_template('Member1.html')
#     return HttpResponse(template.render())


# def submit_membership_form(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         phone_number = request.POST.get('phone_number')
#         email = request.POST.get('email')
#         membership_type = request.POST.get('membership_type')
        
#         # Create a new Membership object and save it to the database
#         Membership.objects.create(
#             full_name=full_name,
#             phone_number=phone_number,
#             email=email,
#             membership_type=membership_type
#         )
        
#         return redirect('Home')  # Redirect to home page after successful submission
#     else:
#         # If it's a GET request or form submission was unsuccessful, render a blank form
#         return render(request, 'Member1.html')
