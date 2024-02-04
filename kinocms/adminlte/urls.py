from django.urls import path
from .views import DashboardView, LoginView, LogoutView

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]
