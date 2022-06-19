from django.urls import path, include
from accounts import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name='account_profile'),
]