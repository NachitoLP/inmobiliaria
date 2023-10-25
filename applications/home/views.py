from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = "home/index.html"

class CatalogueView(TemplateView):
    template_name = "catalogue/index.html"