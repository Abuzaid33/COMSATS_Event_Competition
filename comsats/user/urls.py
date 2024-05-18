from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import CustomLoginView  
from .forms import LoginForm
from .views import  RegisterView
from django.urls import re_path
urlpatterns = [
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', RegisterView.as_view(), name='users-register'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]
