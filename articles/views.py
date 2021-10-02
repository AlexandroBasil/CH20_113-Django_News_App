from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls.base import reverse_lazy
from .models import Articles

class ArticleListView(ListView):
    model = Articles
    template_name = "home.html"

class ArticleDetailView(DetailView):
    model = Articles
    template_name = "article_detail.html"

class ArticleCreateView(CreateView):
    model = Articles
    template_name = "article_create.html"
    fields = ["title", "body", "author", "date"]

class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = "article_update.html"
    fields = ["title", "body", "date"]

class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = "article_delete.html"
    success_url = reverse_lazy("home")