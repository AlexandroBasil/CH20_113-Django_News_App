from django.urls import path
from django.views.generic import TemplateView
from .views import LogInView


urlpatterns = [
    path('signup/', TemplateView.as_view(template_name='home.html'), name='signup'),
]