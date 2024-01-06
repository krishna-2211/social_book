# from tokenize import generate_tokens
from django.shortcuts import redirect, render
from authentication.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserFilter
from django_filters.views import FilterView
from . models import UploadedFile
from . forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from social_book.database import engine
from sqlalchemy import Table, MetaData
import pandas as pd
import numpy as np

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
        is_public = request.POST['is_public']

        if CustomUser.objects.filter(username=username):
            messages.error(request, "Username already exists !")
            return redirect('home')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered !")
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters !")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match !")
        else:
            if is_public == 'on':
                is_public = True
            else:
                is_public = False

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric !")
            return redirect('home')
        
        myuser = CustomUser.objects.create_user(email, pass1)
        myuser.is_public = is_public
        myuser.username = username
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.email = email
        myuser.save()

        messages.success(request, "Your account has been successfully created !")

        return redirect('signin')

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        email = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(email=email, password=pass1)
        
        if user is not None:
            login(request, user)
            # fname = user.first_name
            
            return redirect("options")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully !")
    return redirect('home')

def authors_and_sellers(request):
    try:
        users = CustomUser.objects.all()
        if request.method=="POST":
            print(request)
            print("POST CALLED")
            users=users.filter(is_public=True)
            messages.success(request, "Logged In Successfully!!")
            # print(users)
            return render(request, "authentication/authors_and_sellers.html", {"users": users})
        else:
            print("In else")
            return render(request, "authentication/authors_and_sellers.html", {"users": users})
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return render(request, "authentication/authors_and_sellers.html", {"users": []})

class AuthorsAndSellersView(FilterView):
    model = CustomUser
    template_name = 'authentication/authors_and_sellers.html'
    filterset_class = CustomUserFilter
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CustomUserFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

def options(request):
    return render(request, "authentication/options.html")



@login_required
def upload_books(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user
            file_instance.save()
            return redirect('uploaded_files')
    else:
        form = UploadFileForm()

    return render(request, 'authentication/upload_books.html', {'form': form})

@login_required
def uploaded_files(request):
    files = UploadedFile.objects.all()
    return render(request, 'authentication/uploaded_files.html', {'uploaded_files': files})


def fetch_data(request):
    metadata = MetaData()
    customuser_table = Table('authentication_customuser', metadata, autoload_with=engine)

    with engine.connect() as connection:
        result = connection.execute(customuser_table.select())
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result]

    return render(request, 'authentication/fetch_data.html', {"data": data})



def dataframe(request):
    data = {'Column1': np.random.rand(10),
            'Column2': np.random.randint(1, 100, 10),
            'Column3': np.random.choice(['A', 'B', 'C'], 10)}

    df = pd.DataFrame(data)

    filtered_df = df[df['Column1'] > 0.5]

    filtered_columns_df = df[['Column1', 'Column2']]

    df.replace({'Column2': {73: 999}}, inplace=True)

    dummy_data = {'Column1': np.random.rand(5),
                  'Column2': np.random.randint(1, 100, 5),
                  'Column3': np.random.choice(['A', 'B', 'C'], 5)}

    dummy_df = pd.DataFrame(dummy_data)

    appended_df = pd.concat([df, dummy_df], ignore_index=True)

    return render(request, 'authentication/dataframe.html', {
        'original_df': df.to_html(),
        'filtered_df': filtered_df.to_html(),
        'filtered_columns_df': filtered_columns_df.to_html(),
        'replaced_df': df.to_html(),
        'appended_df': appended_df.to_html(),
    })
