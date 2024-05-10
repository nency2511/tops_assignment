from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

      

        

    
        data = User.objects.filter(username=username,password=password)

        
        if len(data) > 0 :
           for dt in data:
            role = dt.role.role_name
           
            if role == 'customer':
               return render(request,"customer.html", {"name" : dt.username})
            

            else:
                
                
                return render(request,"banker.html", {"name" : dt.username})
        else:
            return render(request,"index.html",{"msg":"Invalid credentials.. please enter valid user"})

    
    return render(request,"index.html")




def reg(request):

    role_object = Roles.objects.all()
    if request.method == 'POST':
        id = request.POST['role']
        username = request.POST['username']
        password = request.POST['password']
        role_data = Roles.objects.get(id = id)
        
        User.objects.create(role = role_data,username=username,password=password)

       
        return render(request,"reg.html",{"role":role_object})

   
    return render(request,"reg.html",{"role":role_object})    



def info(request):

    
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        balance = data.get('balance')
        address = data.get('address')

        User.objects.create(username=username,balance=balance,address=address)
    
    all_data = User.objects.all()
    context = {'all_data':all_data}
    return render(request,'bankcard.html',context)




def delete(requset,id):
    qry_set = User.objects.get(id=id)
    qry_set.delete()
    return redirect('info')

   



def update(request,id):
    std = User.objects.get(id=id)

    if request.method=='POST':
            data = request.POST
            std.name = data.get('username')
            std.password = data.get('password')

            std.save()
            return redirect('index')

    return render(request,'update.html',{"data":std})    



def customer(request):

    
    qryset = User.objects.all()
   
    return render (request, "card.html", {"qryset":qryset})


    

