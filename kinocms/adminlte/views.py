from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm


class DashboardView(TemplateView):
    template_name = "panel/dashboard.html"

    @method_decorator(user_passes_test(lambda u: u.is_staff and u.is_superuser,
                                       login_url="/adminlte/login",
                                       redirect_field_name=None))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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
