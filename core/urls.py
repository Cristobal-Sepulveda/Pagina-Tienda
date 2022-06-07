from django.urls import path
from .views import index, galeria, somos, contacto, modal

urlpatterns=[
    path('', index, name='index'),
    path('galeria/', galeria, name='galeria'),
    path("somos/", somos, name="somos"),
    path("contacto/", contacto, name="contacto"),
    path("modal/", modal, name="modal"),
]