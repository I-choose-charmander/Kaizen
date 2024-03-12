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
    ef1=request.GET.get('extraField1')
    ef2=request.GET.get('extraField2')
    if [x for x in (ef1,ef2) if x == '']:

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
    protien = (request.GET.get('d_protien'))
    carbs = (request.GET.get('d_carb'))
    fats = (request.GET.get('d_fat'))

    if not [x for x in (feet,inches,weight,age) if x == '']:
            Feet = int(feet)
            Inches = int(inches)
            Weight = int(weight)
            Age = int(age)
           

            kg = Weight / 2.205
            cm = (((Feet * 12)+ Inches)*2.54)

            
            protienl = round(Weight * 1.2)
            protienh = round(Weight * 2)
            carbl = round(Weight * 5)
            carbh = round(Weight * 8)
            fatl = round(Weight * .4)
            fath = round(Weight * .5)

            macro_range = {'Protien Low': protienl,'Protien High': protienh,
                              'Carbohydrate Low': carbl, 'Carbohydrate High': carbh, 
                              'Fats Low':fatl, 'Fats High': fath }

            if request.GET.get('checkbox') == "on":
                ans = round(66.47 + (13.75 * kg) + (5.003 * cm) - (6.755 * Age))
                if [x for x in (protien,carbs,fats) if x == '']:
                    return render(request, 'm_results.html', {'ans': ans,'range':macro_range})
                else:
                    Protien = int(protien)
                    Carb= int(carbs)
                    Fat= int(fats)

                    daily_protien_low = protienl - Protien
                    daily_protien_high = protienh - Protien
                    daily_carb_low = carbl - Carb
                    daily_carb_high = carbh - Carb
                    daily_fat_low = fatl - Fat
                    daily_fat_high = fath - Fat
                    
                    macro_range = {'Protien Low': daily_protien_low,'Protien High': daily_protien_high,
                              'Carbohydrate Low': daily_carb_low, 'Carbohydrate High': daily_carb_high, 
                              'Fats Low':daily_fat_low, 'Fats High': daily_fat_high }
                    return render(request, 'm_results.html', {'ans': ans,'range':macro_range})

            
            ans = round(665.1 + (9.563 * kg) + (1.850 + cm) - (4.676 * Age))
            if [x for x in (protien,carbs,fats) if x == '']:
                return render(request, 'm_results.html', {'ans': ans,'range':macro_range})
            else:
                Protien = int(protien)
                Carb= int(carbs)
                Fat= int(fats)

                daily_protien_low = protienl - Protien
                daily_protien_high = protienh - Protien
                daily_carb_low = carbl - Carb
                daily_carb_high = carbh - Carb
                daily_fat_low = fatl - Fat
                daily_fat_high = fath - Fat
                macro_range = {'Protien Low': daily_protien_low,'Protien High': daily_protien_high,
                              'Carbohydrate Low': daily_carb_low, 'Carbohydrate High': daily_carb_high, 
                              'Fats Low':daily_fat_low, 'Fats High': daily_fat_high }
                return render(request, 'm_results.html', {'ans': ans,'range':macro_range})

    ans = 'Error Please try again'
    macro_range= {'Na':0}
    return render(request, 'm_results.html', {'ans': ans,'range':macro_range })
         

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
    api_key = os.getenv('API_KEY_NIX')
    app_id = os.getenv('APP_ID_NIX')
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
        api_key = os.getenv('API_KEY_AFV')
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=KO&interval=5min&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        return render(request, 'display.html',{'data': data})

def stock(request):
    return render(request,"stock.html")