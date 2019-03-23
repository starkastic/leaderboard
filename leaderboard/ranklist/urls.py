from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^input$', views.input, name='input'),
    url(r'^display$', views.display, name='display'),
]
