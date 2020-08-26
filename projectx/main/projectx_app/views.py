from django.shortcuts import render
from django.http import HttpResponse
from projectx_app.models import Blog,Description,AccessRecord
# Importing ContactForm.
from . import forms
from projectx_app.forms import ContactForm
# Importing Sign Up Form.
from projectx_app.models import User
from projectx_app.register import UserForm,UserProfileInfoForm
# Importing Login & Logout Functions.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# setting main index function.
def index(request):
    my_dict = {'insert_me': "Hello there. I am from views.py"}
    return render(request,'projectx_app/index.html',context=my_dict)

# setting bloglist function.
def bloglist(request):
    blog_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':blog_list}
    return render(request,'projectx_app/bloglist.html', context=date_dict)


# set contact form function.
def form_name_view(request):
    form = forms.ContactForm() #form = tu nama dekat html form.as p

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():

# yang ni follow balik dekat forms.py
            print("VALIDATION SUCCESS!")
            print("NAME : "+form.cleaned_data['name'])
            print("EMAIL : "+form.cleaned_data['email'])
            print("ENQUIRY : "+form.cleaned_data['enquiry'])

    return render(request,'projectx_app/about.html',{'form':form})

# Sign Up Page.
def register(request):
    registered = False
    if request.method =="POST":
        user_form = UserForm(data=request.POST)  #user_form kita set dekat html
        profile_form = UserProfileInfoForm( data=request.POST) #profile_form kita set dekat HTML

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'projectx_app/register.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered}) #this is context dictionaries.ada dekat html

# About Page.
def about(request):
    return render(request,'projectx_app/about.html')

# Empty Page.
def empty(request):
    context_dict = {'text':'Hello. This Is Custom Filter. Right Now We have 100 blogs. But now, it is grows to :', 'number':100}
    return render(request,'projectx_app/empty.html',context_dict)

# Login Page.
def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index')) #if user berjaya login, will redirect to homepage

            else:
                return HttpResponse("Your Account Is Not Active. Please Sign Up.")

        else:
            print("Someone tried to login and failed") # if ada org test username/password tapi salah
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("hey, you key in an invalid login details!")

    else: #if dia x masukkan apa2 username n password
        return render(request,'projectx_app/login.html',{})

# Welcome Wording (For login user).
@login_required
def special(request):
    return HttpResponse("You're now logged in, Nice!")

# Logout Function.
@login_required  #maksudnya, bende ni hanya function if user dah login
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
