from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def Index (request):
    if request.method == 'POST':
        data = request.POST
        pname = data.get('pname')
        price = data.get('price')
        qty = data.get('qty')
        ram = data.get('ram')



        Product.objects.create(pname=pname,price=price,qty=qty,ram=ram)
    
    all_data = Product.objects.all()
    context = {'all_data':all_data}
    return render(request,'index.html',context)



def delete(requset,id):
    qry_set = Product.objects.get(id=id)
    qry_set.delete()
    # return redirect("index.html")  
    return redirect('index')

   



def update(request,id):
    std = Product.objects.get(id=id)

    if request.method=='POST':
            data = request.POST
            std.pname = data.get('pname')
            std.price = data.get('price')
            std.qty = data.get('qty')
            std.ram = data.get('ram')


            std.save()
            return redirect('index')

    return render(request,'update.html',{"data":std})    

