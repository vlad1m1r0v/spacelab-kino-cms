from django.urls import path
from adminlte.views.authentication import LoginView, LogoutView

app_name = "authentication"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout")
]
