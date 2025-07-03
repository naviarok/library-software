from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Formulaire
from django.db.models import Q

# EXCEL MODULE
from openpyxl import Workbook

# USER MANIPULATION MODULES
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# OTHER
from datetime import datetime
import os

# developer
# lolo12345

# return current date and time
def get_today_date_str():
    now = datetime.now()
    return now.strftime("%H:%M:%S  %d/%m/%y")


# home page containing a form
def Home(request):
    if request.method == 'POST':
        try:
            firstName = request.POST.get('first', '-')
            lastName = request.POST.get('last', '-')
            fillier = request.POST.get('fillier', '-')
            code = request.POST.get('code', '-')
            items = request.POST.get('items', '-')
            Formulaire.objects.create(FirstName=firstName, LastName=lastName, Code=code, Items=items, Date=get_today_date_str(), Fillier=fillier)
            return redirect('success')
        except:
            return redirect('error')
    return render(request, 'formulaire/index.html')


# success page showing the validation of conntent
def Success(request):
    return render(request, 'formulaire/success.html')

# error page
def Error(request):
    return render(request, 'formulaire/error.html')

# redirect automatically to home page
def HomeRedirect(request):
    return redirect('home')

# generate an Excel file containing all the database data
@login_required(login_url='login')
def ExportExcel(request):
    path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'MyworkBook.xlsx') 
    wb = Workbook()
    ws = wb.active
    ws.title = 'student logs'
    ws.append(['nom', 'prenom', 'fillier', 'code', 'items', 'date'])
    for data in Formulaire.objects.all():
        ws.append([data.FirstName, data.LastName, data.Fillier, data.Code, data.Items, data.Date])
    try:
        wb.save(path)
    except:
        return render(request, 'formulaire/efail.html')
    return render(request, 'formulaire/esuc.html')


def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('table')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, '  ', password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('table')
        else:
            return redirect('home')
    return render(request, 'formulaire/login.html')

def LogoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def Table(request):
    data = Formulaire.objects.all()
    notFound = 0 

    if request.method == "POST":
        search = request.POST.get('search')
        data = Formulaire.objects.filter(
            Q(FirstName__icontains=search) |
            Q(LastName__icontains=search) |
            Q(Fillier__icontains=search) |
            Q(Code__icontains=search) |
            Q(Items__icontains=search) |
            Q(Date__icontains=search)
        )
        if len(data) == 0:
            notFound = 1

    context = {'data': data, 'not_found': notFound}
    return render(request, 'formulaire/table.html', context)