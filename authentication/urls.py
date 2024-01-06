from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('signin', views.signin, name='signin'),
    path('authors_and_sellers', views.authors_and_sellers, name='authors_and_sellers'),
    path('options', views.options, name='options'),
    path('upload_books', views.upload_books, name='upload_books'),
    path('uploaded_files', views.uploaded_files, name='uploaded_files'),
    path('fetch_data', views.fetch_data, name='fetch_data'),
    path('dataframe', views.dataframe, name='dataframe'),
]

