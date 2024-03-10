from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm



# Create your views here.



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
        else:
            ans = 'Error Please try again'
            return render(request, 'm_results.html', {'ans': ans})

def c_results(request):
    cal = 0
    protien = int(request.GET.get('protien'))
    fat = int(request.GET.get('fat'))
    carb = int(request.GET.get('carb'))
    if request.GET.get('breakdown') == "":
         cal += ((protien * 4) + (fat * 9) + (carb * 4))
         return render(request, 'c_results.html', {'ans': cal })

         
    return render(request, 'c_results.html', {'ans': cal })

