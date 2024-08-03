from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib import auth
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from users.forms import UserLoginForm

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('main:index')
    
    def form_valid(self, form):

        user = form.get_user()

        if user:
            auth.login(self.request, user)

        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Авторизация'
        return context
    
    

class RegistrationView():
    ...
