import os
import requests, json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from .models import *
from .forms import *


# Create your views here.

load_dotenv()
DATABASE_ACCESS = True

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

            macro_range = {'Protien Low to High': [protienl,protienh],
                              'Carbohydrate Low to High': [carbl,  carbh], 
                              'Fats Low to High': [fatl, fath] }
            pro_macro = []
            pro_macro.append(macro_range['Protien Low to High'][0:2])
            pro_macro.append(macro_range['Carbohydrate Low to High'][0:2])
            pro_macro.append(macro_range['Fats Low to High'][0:2])

            if request.GET.get('checkbox') == "on":
                ans = round(66.47 + (13.75 * kg) + (5.003 * cm) - (6.755 * Age))
                if [x for x in (protien,carbs,fats) if x == '']:
                    return render(request, 'm_results.html', {'ans': ans,'range':macro_range,'new':pro_macro})
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
                    
                    macro_range = {'Protien Low to High': [daily_protien_low , daily_protien_high],
                              'Carbohydrate Low to High': [daily_carb_low, daily_carb_high], 
                              'Fats Low to High':[daily_fat_low, daily_fat_high]}
                
                    pro_macro = []
                    pro_macro.append(macro_range['Protien Low to High'][0:2])
                    pro_macro.append(macro_range['Carbohydrate Low to High'][0:2])
                    pro_macro.append(macro_range['Fats Low to High'][0:2])
                    return render(request, 'm_results.html', {'ans': ans,'range':macro_range, 'new':pro_macro})

            ans = round(665.1 + (9.563 * kg) + (1.850 + cm) - (4.676 * Age))
            if [x for x in (protien,carbs,fats) if x == '']:
                return render(request, 'm_results.html', {'ans': ans,'range':macro_range,'new':pro_macro})
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
                macro_range = {'Protien Low to High': [daily_protien_low, daily_protien_high],
                              'Carbohydrate Low to High': [daily_carb_low, daily_carb_high], 
                              'Fats Low to High':[daily_fat_low, daily_fat_high]}
                
                pro_macro = []
                pro_macro.append(macro_range['Protien Low to High'][0:2])
                pro_macro.append(macro_range['Carbohydrate Low to High'][0:2])
                pro_macro.append(macro_range['Fats Low to High'][0:2])
                return render(request, 'm_results.html', {'ans': ans,'range':macro_range,'new':pro_macro})

    ans = 'Error Please try again'
    macro_range= {'Na':0}
    pro_macro = []
    return render(request, 'm_results.html', {'ans': ans,'range':macro_range, 'new':pro_macro})
         

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
    form = FoodForm()
    return render(request,"Food.html",{'form':form})

def get_api_data(request):
    query = request.POST.get('food')
    api_key = os.getenv('API_KEY_NIX')
    app_id = os.getenv('APP_ID_NIX')
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers={
            'Content-Type': 'application/json',
            'x-app-id': app_id,
            'x-app-key': api_key,
                }
    search = {
         'query' : query 
    }

    response = requests.post(url,headers=headers,data=json.dumps(search))
    if response.status_code == 200:
        data2 = response.json()
        for item in data2['foods']:
             #data.append(item)
             
             serving = item['serving_unit']
             grams = item['serving_weight_grams']
             calories_of_food = item['nf_calories']
             fats = item['nf_total_fat']
             carbo = item['nf_total_carbohydrate']
             protien = item['nf_protein']

             data = {'Food': query, 'Serving_size': serving, 'Grams':grams,
                     'Calories': calories_of_food, 'Protien':protien, "Carbohydrates":carbo, 'Fats':fats}

             
        return render(request, 'display.html', {'data': data})
    error= f'Request failed with status code {response.status_code}'
    return render(request, 'display.html', {'data': error})

def stock_api_data(request):
        ticker = request.POST.get('ticker', 'null')
        api_key = os.getenv('API_KEY_AFV')
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=KO&interval=5min&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        return render(request, 'display.html',{'data': data})

def stock(request):
    return render(request,"stock.html")
