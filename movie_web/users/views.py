from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .forms import RegisterUserForm

class Login(LoginView):
    template_name = "users/accounts/login.html"

class Logout(LogoutView):
    next_page = "/"

class RegisterUser(FormView):
    template_name = "users/accounts/register.html"
    form_class = RegisterUserForm
    success_url = "/thanks/"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


@login_required
def profile(request):
    user = request.user
    return render(request,"users/accounts/profile.html",{"user":user})