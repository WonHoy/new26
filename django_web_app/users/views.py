from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import ast
import datetime as dt
from .py5110lug import *
import math
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)



@csrf_exempt
def lug(request):
    template = 'users/index5110.html'
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
