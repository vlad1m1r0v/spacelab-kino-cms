from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.contrib.auth import login, logout, authenticate
from .mixins import AdminPermissionMixin
from users.forms import LoginForm


class DashboardView(AdminPermissionMixin, TemplateView):
    template_name = "adminlte/index.html"


class LoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,
                                password=password,
                                is_superuser=True)
            if user:
                login(request, user)
                return redirect('dashboard')
        template = 'adminlte/login.html'
        context = {'login_form': form}
        return render(request, template, context)

    def get(self, request):
        template = 'adminlte/login.html'
        context = {'login_form': LoginForm()}
        return render(request, template, context)


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect("/adminlte/login")
