from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm

# Create your views here.
### vista basada en clase para hacer el registro de usuario ###
class RegistroUsuarioView(FormView):
    template_name = 'users/registro.html'
    form_class = RegistroForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return redirect('login')

### vista basada en clase para iniciar sesión ###
class LoginUsuarioView(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm

class LogoutUsuarioView(LogoutView):
    pass