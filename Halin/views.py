import datetime 
from django.db.models import Sum, Avg, Count


from django.shortcuts import render
from .models import *
from django.utils import timezone

# Create your views here.

def Halin(request):
    timezone.now().date()

    displaydata = LugawanHalin.objects.all().order_by('transdate')
    totalhalin = 0
    totalgasto = 0
    kita = 0
  

   
    expensesresult = LugawanExpense.objects.all().order_by('transdate')
    if request.method == "POST":
        #displaydata = LugawanHalin.objects.all().order_by('-transdate')
        
        #fromdate = timezone.now().date()
        #todate = timezone.now().date()+ datetime.timedelta(days=1)
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        
        print(fromdate)
        #displaydata = LugawanHalin.objects.filter(transdate__range=[fromdate, todate])
        #displaydata = LugawanHalin.objects.filter(transdate__gte=datetime.date(2, 6, 4), transdate__lte=datetime.date(2025, 1, 31))
        displaydata = LugawanHalin.objects.filter(transdate__range=[fromdate,todate]).order_by('-transdate')
        expensesresult = LugawanExpense.objects.filter(transdate__range=[fromdate,todate]).order_by('-transdate')
        totalhalin = list(LugawanHalin.objects.filter(transdate__range=[fromdate,todate]).aggregate(Sum('price')).values())[0]
        totalgasto = list(LugawanExpense.objects.filter(transdate__range=[fromdate,todate]).aggregate(Sum('price')).values())[0]
        
        if totalhalin is None:
            totalhalin = 0
        
        if totalgasto is None:
            totalgasto = 0

        kita = totalhalin - totalgasto
        print(displaydata)
    context= {
        'Tananhalin':displaydata,
        'Totalkita': totalhalin,
        'Totalgasto': totalgasto,
        'Tanankita': kita,
        'Expensesview':expensesresult,
        }
       

    
    return  render(request, ('index.html'), context)
