from django.urls import path
from .views import *

urlpatterns = [
    # front
    path('all/', all, name='about'),
    path('blog/', blog, name='blog'),
    path('categori/', categori, name='categori'),
    path('contact/', contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('', index, name='index'),
    # path('details/', details, name='details'),
    # path('latest_news/', latest_news, name='latest_news'),
    # path('main/', main, name='main'),
    # path('singleblog/', singleblog, name='singleblog'),

    # dashboard
    path('dashboard/', dashboard_index, name='index')
]