from django.urls import path
from . import views
from .views import GenerateToken, FileView
from django.contrib.auth import views as auth_views

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
    path('my_books', views.my_books_dashboard, name='my_books_dashboard'),
    path('login', GenerateToken.as_view(), name='login'),
    path('files', FileView.as_view(), name='file-access'),
    # Change this line in your urls.py
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_sent.html'), name='password_rest_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
]

