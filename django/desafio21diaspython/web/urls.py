from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
  path('', views.index),
  path('about', views.about),
  path('contact', views.contact),
  path('post', views.post),
  path('json', views.json),
  path('html_bruto', views.html_bruto),
  path('xml_bruto', views.xml_bruto),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)