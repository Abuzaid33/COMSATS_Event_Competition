
from django.contrib import admin
from django.urls import path,include
from user.views import ResetPasswordView
from django.contrib.auth import views as auth_views
from user.views import ChangePasswordView

    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('user.urls')),
    path('', include('chatbot.urls')),
    path('', include('ChatApp.urls')),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]
