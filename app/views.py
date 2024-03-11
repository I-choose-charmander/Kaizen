from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib import messages
from django.views import View
import os
from dotenv import load_dotenv
import requests, json
# Create your views here.

load_dotenv()

def home(request):
    template= loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def finance(request):
    return render(request,"finance.html")

def macro(request):
    return render(request,"macro.html")
def calories(request):
    return render(request,"calories.html")

def f_results(request):
    income= int(request.GET.get('inc'))

    if request.GET.get('breakdown') == "":

        personal = income * .2
        saving = income * .3
        essentials = income * .5

        answer = {"Personal":personal,"Saving":saving, "Essential":essentials}


    return render(request, 'f_results.html', {'ans': answer})
   
def m_results(request):
    feet = (request.GET.get('feet'))
    inches = (request.GET.get('inches'))
    weight = (request.GET.get('weight'))
    age = (request.GET.get('age'))

    if request.GET.get('breakdown') == "":
        if not [x for x in (feet,inches,weight,age) if x == '']:
            Feet = int(feet)
            Inches = int(inches)
            Weight = int(weight)
            Age = int(age)

            kg = Weight * 2.2
            cm = (((Feet * 12)+ Inches)*2.54)

            if request.GET.get('checkbox') == "on":
                ans = 66.47 + (13.75 * kg) + (5.003 * cm) - (6.755 * Age)
                return render(request, 'm_results.html', {'ans': ans})
            
            ans = 665.1 + (9.563 * kg) + (1.850 * cm) - (4.676 * Age)
            return render(request, 'm_results.html', {'ans': ans})

        ans = 'Error Please try again'
        return render(request, 'm_results.html', {'ans': ans})

def c_results(request):
    cal = 0
    protien = int(request.GET.get('protien'))
    fat = int(request.GET.get('fat'))
    carb = int(request.GET.get('carb'))
    if request.GET.get('breakdown') == "":
        if not [x for x in (protien,fat,carb) if x == '']:
            cal += ((protien * 4) + (fat * 9) + (carb * 4))
            return render(request, 'c_results.html', {'ans': cal })
        else:
            cal = 'Error Please try again'
            return render(request, 'c_results.html', {'ans': cal })

def food(request):
    return render(request,"Food.html")

def get_api_data(request):
    query = request.GET.get('food')
    api_key = os.getenv('API_KEY')
    app_id = os.getenv('APP_ID')
    url = "https://trackapi.nutritionix.com/v2/search/instant"
    headers={
            'x-app-id': app_id,
            'x-app-key': api_key,
                }
    response = requests.get(url,headers=headers,params={"query": query})
    if request.GET.get('breakdown') == "":
        if response.status_code == 200:
            data = response.json()
            return render(request, 'display.html', {'data': data})
        data = 'Request failed with status code {response.status_code}'
        return render(request, 'display.html', {'data': data})

def stock_api_data(request):
        ticker = request.POST.get('ticker', 'null')
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=KO&interval=5min&apikey=HASIDZ04KY62WNJD'

        headers = {
            'x-app-id': "HASIDZ04KY62WNJD",
        }
        response = requests.get(url)
        data = response.json()
        return render(request, 'display.html',{'data': data})

def stock(request):
    return render(request,"stock.html")