from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import django_filters
from .models import UploadedFile

class CustomUserCreationForm(UserCreationForm):
    is_public = forms.BooleanField(label="Make my profile public")
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "is_public", "fname", "lname")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "is_public", "fname", "lname")

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "fname", "lname"]

class CustomUserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = ['is_public']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'description', 'visibility', 'cost', 'year_published', 'file']

