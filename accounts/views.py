from django.views.generic.edit import CreateView


class LogInView(CreateView):
    template_name = "login.html"