from django.shortcuts import render,HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Max 
from django.db.models import Q


# Create your views here.
global search_data
def index (request):

    
    queryset = Student.objects.all()

    if request.GET.get("search"):
        search_data = request.GET.get("search")
        queryset = Student.objects.filter(name__icontains=search_data)


    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render (request, "index.html", {"qryset":page_obj})







def marks(request,id):

    ranks = Student.objects.annotate(marks = Sum('studentmark__marks')).order_by('-marks')
    i =1
    current_rank = 0
    for rank in ranks:
        if rank.student_id.student_id ==id:
            current_rank=i
        i = i+1    
    qryset = StudentMark.objects.filter(student__student_id__student_id = id)
    total = qryset.aggregate(total =Sum('marks'))
    avg = qryset.aggregate(avg=Avg('marks'))
    max = qryset.aggregate(max=Max('marks'))  
    return render (request, "card.html", {"qryset":qryset, "total":total, "avg":avg, "max":max, "rank":current_rank})


   


    
        