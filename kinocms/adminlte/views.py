from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.contrib.auth import login, logout, authenticate

from .decorators import admin_only
from .forms import LoginForm


@admin_only
class DashboardView(TemplateView):
    template_name = "panel/dashboard.html"


class LoginView(View):
    @staticmethod
    def post(request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password, is_superuser=True)
            if user:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Incorrect email or password")
        template = "authentication/login.html"
        context = {"login_form": form}
        return render(request, template, context)

    @staticmethod
    def get(request):
        template = "authentication/login.html"
        context = {"login_form": LoginForm()}
        return render(request, template, context)


class LogoutView(View):
    @staticmethod
    def post(request):
        logout(request)
        return redirect("/adminlte/login")
