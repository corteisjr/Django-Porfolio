from django.urls import path
from myPortfolio.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path("<int:id>", list_projects, name='profile'),
]
