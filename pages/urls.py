from django.urls import path
# Sem templates
#from . import views
#Ou usando template
from .views import AboutPageView, HomePageView

app_name = "pages"

urlpatterns = [
    #path("about/", views.AboutPageView, name="about"),
    #path("", views.HomePageView, name="home"),
    #usando templates
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    
]
