from django.views.generic import TemplateView
# Create your views here.
class DisplayTemplate(TemplateView):
    template_name = 'home.html'