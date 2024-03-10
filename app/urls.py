from django.urls import path
from app import views
from .views import home, calories, finance,macro,f_results,m_results, c_results
from django.conf import settings


urlpatterns = [
    path("", home, name="home"),
    path("finance/", finance, name="finance"),
    path("macro/", macro, name="macro"),
    path("f_results/", f_results, name='f_results'),
    path("m_results/",m_results, name='m_results'),
    path("calories/", calories , name='calories'),
    path("c_results/",c_results, name='c_results'),
]  