from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import User

#### este es el formulario para registrar una nueva cuenta ####
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'nombre', 'apellido', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'required': 'true'
            })

#### este es el formulario para iniciar sesion ####
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario o Correo',required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if '@' in username:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            try:
                user = User.objects.get(email=username)
                username = user.username
            except User.DoesNotExist:
                raise forms.ValidationError('Correo electrónico no encontrado.')

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Credenciales incorrectas.')

        self.user_cache = user  

        self.confirm_login_allowed(user)
        return self.cleaned_data

    def get_user(self):
        return getattr(self, 'user_cache', None)