from django.shortcuts import render
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import PostForm
from django.http import HttpResponseRedirect






# Create your views here.
def add_post(request):
    submitted=False
    if request.method == "POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            
            return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form=PostForm   
        if 'submitted' in request.GET:
            submitted=True
        
    
    return render(request,'module_image/add_post.html', {'form':form, 'submitted':submitted})  






def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # conversion du mois du nom au numero
    month=month.title()
    month_number= list(calendar.month_name).index(month)
    month_number=int(month_number)
    
    # Creation du calendrier
    cal=HTMLCalendar().formatmonth(year, month_number)
    
    # Les dates
    now=datetime.now()
    current_year=now.year
    current_month=now.month
    current_day=now.day
    
    # Time
    time=now.strftime("%I:%M:%S")
    
    nom="john"
    return render(request, 'home.html', {
        "nom":nom,
        "year":year,
        "month":month,
        "month_number":month_number,
        "cal":cal,
        "current_year": current_year,
        "time": time,
        "current_day": current_day,
        }) 
