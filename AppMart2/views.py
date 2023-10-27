from django.shortcuts import render,redirect
from AppMart.models import CategoryDB,ProductDB
from AppMart2.models import RegistrationDB,CartDB,CheckoutDB
from django.contrib import messages


# Create your views here.

def homepage(request):
    data = CategoryDB.objects.all()
    return render(request,"Home.html",{'data':data})

def productpage(request,pro_name):
    data = ProductDB.objects.filter(CategoryName=pro_name)
    return render(request,"Products.html",{'data':data})

def singlepro(request,dataid):
    data = ProductDB.objects.get(id=dataid)
    return render(request,"SingleProduct.html",{'data':data})
def aboutpage(request):
    data = CategoryDB.objects.all()
    return render(request,"Aboutus.html",{'data':data})
def contactpage(request):
    data = CategoryDB.objects.all()
    return render(request,"Contact.html",{'data':data})
def user_regpage(request):
    return render(request,"user_reg.html")
def save_data(request):
    if request.method=="POST":
        un = request.POST.get('u_name')
        um = request.POST.get('u_mail')
        pd = request.POST.get('u_password')
        mob = request.POST.get('u_mobile')
        img = request.FILES['u_img']
        obj = RegistrationDB(Username=un,Mail=um,Password=pd,Mobile=mob,Image=img)
        obj.save()
        return redirect(userlogin)
def userlogin(request):
    return render(request,"UserLogin.html")
def User_Login(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if RegistrationDB.objects.filter(Username=uname, Password=pwd).exists():
            request.session['Username'] = uname
            request.session['Password'] = pwd
            return redirect(homepage)
        else:
            return redirect(userlogin)
    return redirect(userlogin)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(userlogin)
def save_data1(request):
    if request.method=="POST":
        usern = request.POST.get('user_name')
        pro = request.POST.get('pro_name')
        quant = request.POST.get('quantity')
        tot = request.POST.get('total')
        obj = CartDB(Username=usern,ProductName=pro,Quantity=quant,TotalPrice=tot)
        obj.save()
        return redirect(homepage)
def displaycart(request):
    data = CartDB.objects.filter(Username=request.session['Username'])
    total_price = 0
    for i in data:
        total_price = total_price+i.TotalPrice
    return render(request,"Cart.html",{'data':data,'total_price':total_price})
def deletecart(request,dataid):
    data = CartDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycart)
def checkout(request):
    return render(request,"checkout.html")

def save_data3(request):
    if request.method=="POST":
        name = request.POST.get('us_name')
        con = request.POST.get('country')
        st = request.POST.get('state')
        add = request.POST.get('address')
        mail = request.POST.get('eemail')
        town = request.POST.get('town')
        pho = request.POST.get('phone')
        obj = CheckoutDB(Name=name,Country=con,State=st,Address=add,Email=mail,Town=town,Phone=pho)
        obj.save()
        messages.success(request, "Order Placed Successfully...")
        return redirect(homepage)