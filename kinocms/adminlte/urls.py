from django.urls import path
from .views import DashboardView, LoginView

urlpatterns = [
    path('dashboard', DashboardView.as_view()),
    path('login', LoginView.as_view())
]
