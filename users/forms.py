from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", required=True)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise ValidationError("E-mail inexistente.")

            user = authenticate(email=user.email, password=password)
            if user is None:
                raise ValidationError("Senha inválida.")

        return cleaned_data


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['nome', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['nome'] 
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está em uso.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas não coincidem.")

        if len(password1) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")

        if not any(char.isdigit() for char in password1):
            raise ValidationError("A senha deve conter pelo menos um número.")

        if not any(char.isupper() for char in password1):
            raise ValidationError("A senha deve conter pelo menos uma letra maiúscula.")

        if not any(char in '!@#$%^&*()' for char in password1):
            raise ValidationError("A senha deve conter pelo menos um caractere especial.")

        return password2