from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib import auth
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from users.forms import UserLoginForm, UserRegistrationForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('main:index')
    extra_context = {'title': 'Авторизация'}
    
    def form_valid(self, form):

        user = form.get_user()

        if user:
            auth.login(self.request, user)

        return HttpResponseRedirect(self.success_url)
    

class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('main:index')
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):

        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)

        return HttpResponseRedirect(self.success_url)
    
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
