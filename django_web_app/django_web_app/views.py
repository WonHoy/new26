from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import ast
import datetime as dt
from .py5110lug import *
import math
from .forms import *
# TODO: Need to think what should we do with main index page. Create separate app?
#def index(request):
#    template = 'pt_applications/pin.html'
#    return render(request, template)

@csrf_exempt
def lug(request):
    template = '5110lug/index5110lug.html'
    if request.method == "POST":
        submitbutton= request.POST.get("Submit")
#Material        
        form= Mat5110(request.POST)
        Material="Start"
        Specification="of"
        Temper="table"
        if form.is_valid():
            Ref= form.cleaned_data.get("Ref")
            Material= form.cleaned_data.get("Material")
            Specification= form.cleaned_data.get("Specification")
            Temper= form.cleaned_data.get("Temper")
            Form= form.cleaned_data.get("Form")
            tb=  form.cleaned_data.get("tb")
            Basis= form.cleaned_data.get("Basis")
            Grain= form.cleaned_data.get("Grain")
            GrainT= form.cleaned_data.get("GrainT")
            naxu= form.cleaned_data.get("naxu")
            Ntru= form.cleaned_data.get("Ntru")
            Ftuax= form.cleaned_data.get("Ftuax")
            Ftutr= form.cleaned_data.get("Ftutr")
        (naxu,Ntru)=tablenaxu(Material,Temper,Form,tb,Grain,GrainT,naxu,Ntru)
        Ftuax=30001
        Ftutr=60000
        Ftuax=tableFtu(Material,Temper,Basis,tb,Grain,Ftuax)
        Ftutr=tableFtu(Material,Temper,Basis,tb,GrainT,Ftutr)
#Geometry        
        form= Geometry5110(request.POST)
        e="Start"
        R="of"
        D="table"
        t="Start"
        beta="of"
        theta="table"
        if form.is_valid():
            e= form.cleaned_data.get("e")
            R= form.cleaned_data.get("R")
            D= form.cleaned_data.get("D")
            t= form.cleaned_data.get("t")
            beta= form.cleaned_data.get("beta")
            theta= form.cleaned_data.get("theta")
        data_input = {
            'e': e,
            'R': R,
            'D': D,
            't': t,
            'beta': beta,
            'theta': theta,
            'naxu': naxu,
            'Ntru': Ntru,
            'Ftuax': Ftuax,
            'Ftutr': Ftutr,
        }
        try:
          f = open('.\\5110lug\\LOG\\log_5110lug.txt', 'a')
          f.write(str(data_input)+"\n")
          data_output=py5110lug_calc(data_input)
          f.write(str(data_output)+"\n")
          f.close()
        except FileNotFoundError:
            pass
        context=data_output
        try:
            f = open('.\\5110lug\\LOG\\lug.txt', 'a')
            f.write(str(submitbutton)+"\n")
            f.write(str(request)+"\n")
            f.write(str(request.POST)+"\n")
            f.write(str(context)+"\n")
            f.write(str(dt.datetime.today())[0:19]+"\n")
            f.close()
        except FileNotFoundError:
            pass
    else:
        context={
            'e': 2,
            'R': 2,
            'D': 1.2,
            't': 1.2,
            'beta': 0,
            'theta': 0,
            'naxu': 2,
            'Ntru': 4,
            'Ftuax': 30001,
            'Ftutr': 60000,
            'datatime': 'Calculated Lug8_Spline.xls: 2004-03-22 17:08'
        }
        try:
            f = open('.\\5110lug\\LOG\\lug.txt', 'a')
            f.write(str(request)+"\n")
            f.write(str(request.GET)+"\n")
            f.write(str(context)+"\n")
            f.write(str(dt.datetime.today())[0:19]+"\n")
            f.close()
        except FileNotFoundError:
            pass
    return render(request, template, context)
    
def new13(request):
    if request.method == "POST":
        submitbutton= request.POST.get("Submit")
        form= Form13(request.POST)
        tab01="Start"
        tab02="of"
        if form.is_valid():
            tab01= form.cleaned_data.get("tab01")
            tab02= form.cleaned_data.get("tab02")
        tab01=tab01+"Start"
        tab02=tab02+"of"
        context={ "tab01": tab01, "tab02": tab02, "tab03": tab03, "tab04": tab04}
        try:
            f = open('.\\new13.txt', 'a')
            f.write(str(submitbutton)+"\n")
            f.write(str(request)+"\n")
            f.write(str(request.POST)+"\n")
            f.write(str(context)+"\n")
            f.write(str(dt.datetime.today())[0:19]+"\n")
            f.close()
        except FileNotFoundError:
            pass
    else:
        context={ "tab01": "?Start", "tab02": "?of", "tab03": "?table", "tab04": "?!"}
    return render(request, "5013new13/index5013new13.html", context)

def new14(request):
    if request.method == "POST":
        submitbutton= request.POST.get("Submit")
        form= Form14(request.POST)
        name14a=""
        name14b=""
        name14c=""
        name14d=""
        name14e=""
        name14f=""
        if form.is_valid():
            name14a= form.cleaned_data.get("name14a")
            name14b= form.cleaned_data.get("name14b")
            name14c= form.cleaned_data.get("name14c")
            name14d= form.cleaned_data.get("name14d")
            name14e= form.cleaned_data.get("name14e")
            name14f= form.cleaned_data.get("name14f")
        context={'form': form}
        try:
            f = open('.\\new14.txt', 'a')
            f.write(str(submitbutton)+"\n")
            f.write(str(request)+"\n")
            f.write(str(request.POST)+"\n")
            f.write(str(context)+"\n")
            f.write(str(dt.datetime.today())[0:19]+"\n")
            f.close()
        except FileNotFoundError:
            pass
    else:
        form= Form14()
        context={'form': form, "name14b": "1111", "name14d": "22222", "name14f": "33333333333"}
    return render(request, "5014new14/index5014new14.html", context)

@csrf_exempt
def lug_calc(request):
    if request.method == 'POST':
       data_input =ast.literal_eval(request.body.decode('utf-8') )
       try:
          f = open('.\\5110lug\\LOG\\log_5110lug.txt', 'a')
          f.write(str(data_input)+"\n")
          data_output=py5110lug_calc(data_input)
          f.write(str(data_output)+"\n")
          f.close()
       except FileNotFoundError:
              pass
       return JsonResponse(data_output)
