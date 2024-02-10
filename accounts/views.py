from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import User


class CreateUser(LoginRequiredMixin, CreateView):
    model = User
    fields = ["email", "first_name", "last_name", "password"]
    template_name = "accounts/create_user.html"
    success_url = reverse_lazy("user_list")


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["email", "first_name", "last_name", "password"]
    template_name = "accounts/update_user.html"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        return super().form_valid(form)


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "accounts/delete_user.html"
    success_url = reverse_lazy("user_list")


class UserList(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "users"
    template_name = "accounts/user_list.html"


class Login(View):
    template_name = "accounts/login.html"
    
    def get(self, request):
        form = AuthenticationForm
        return render(request, self.template_name, {"form": form})

    def post(self, request):  
        email = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("user_list")
        else:
            form = AuthenticationForm
            return render(
                request, self.template_name, {"error": form.error_messages, "form": form}
            )


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("index")
