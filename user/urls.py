from django.urls import path
from . import views

urlpatterns=[
path("index/",views.index),
path("",views.index),
path("about/",views.about),
path("contact/",views.contact),
path("gallery/",views.gallery),
path("team/",views.team),
path("booking/",views.booking),
path("offers/",views.offers),
path("menu/",views.menu),
path("developer/",views.developer),
]