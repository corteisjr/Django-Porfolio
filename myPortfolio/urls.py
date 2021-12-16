from django.urls import path
from myPortfolio.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path("about", about, name='about'),
]
