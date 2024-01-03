# from tokenize import generate_tokens
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from social_book import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
# from . models import UserProfile

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists !")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered !")
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters !")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match !")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric !")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.username = username
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.email = email
        myuser.save()

        messages.success(request, "Your account has been successfully created !")

        return redirect('signin')

    return render(request, "authentication/signup.html")


# def activate(request,uidb64,token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk=uid)
#     except (TypeError,ValueError,OverflowError,User.DoesNotExist):
#         myuser = None

#     if myuser is not None and generate_token.check_token(myuser,token):
#         myuser.is_active = True
#         # user.profile.signup_confirmation = True
#         myuser.save()
#         login(request,myuser)
#         messages.success(request, "Your Account has been activated!!")
#         return redirect('signin')
#     else:
#         return render(request,'activation_failed.html')


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            username = user.username
            # fname = user.first_name
            # lname = user.last_name
            # email = user.email

            messages.success(request,"You have successfully logged in!")
            return redirect('display')

        else:
            messages.error(request, "Bad credentials !")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully !")
    return redirect('home')

def display(request):
    users= User.objects.all()
    print(users)
    return render (request, "authentication/display.html", {"users":users})

