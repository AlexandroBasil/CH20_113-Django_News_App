from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from .forms import CustomUserCreationForm


class LogInView(CreateView):
    template_name = "login.html"

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"