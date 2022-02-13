from django.shortcuts import render
#from django.http import HttpResponse
# TemplateView usa classes
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"
class AboutPageView(TemplateView):
    template_name = "about.html"    

def is_ajax(request):
    if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        return True

    if request.content_type == "application/json":
        return True
    return False    

