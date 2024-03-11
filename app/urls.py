from django.urls import path,include
from app import views
from .views import home,stock,calories,stock_api_data,food,finance,macro,f_results,m_results, c_results, get_api_data
from django.conf import settings





urlpatterns = [
    path("", home, name="home"),
    path("finance/", finance, name="finance"),
    path("macro/", macro, name="macro"),
    path("f_results/", f_results, name='f_results'),
    path("m_results/",m_results, name='m_results'),
    path("calories/", calories , name='calories'),
    path("c_results/",c_results, name='c_results'),
    path('api-data/',get_api_data, name='api-data'),
    path('food/', food, name='food'),
    path('stocks/', stock, name='stock'),
    path('stock-api-data/',stock_api_data, name='stock-api-data'),
]  