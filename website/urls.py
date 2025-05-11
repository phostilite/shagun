from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('packages/', views.packages, name='packages'),
    path('venues/', views.venues, name='venues'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
]

# Custom error handlers
handler404 = 'website.views.page_not_found'
handler500 = 'website.views.server_error'
