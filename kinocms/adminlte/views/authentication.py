from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import login, logout, authenticate

from adminlte.forms.authentication import LoginForm


class LoginView(TemplateView):
    template_name = "authentication/login.html"

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password, is_superuser=True)
            if user:
                login(request, user)
                return redirect("dashboard:index")
            else:
                messages.error(request, "Incorrect email or password")
        context = {"form": form}
        return self.render_to_response(context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm()
        return context


class LogoutView(View):
    @staticmethod
    def post(request):
        logout(request)
        return redirect("authentication:login")
