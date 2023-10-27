from django.shortcuts import render,redirect
from AppMart.models import CategoryDB,ProductDB
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.

def indexpage(request):
    return render(request,"index.html")

def addcategory(request):
    return render(request,"AddCategory.html")
def savedata(request):
    if request.method=="POST":
        cn = request.POST.get('c_name')
        des = request.POST.get('c_description')
        img = request.FILES['c_img']
        obj = CategoryDB(CategoryName=cn,Description=des,Image=img)
        obj.save()
        messages.success(request,"Category Saved Successfully...")
        return redirect(addcategory)
def displaycategory(request):
    data = CategoryDB.objects.all()
    return render(request,"DisplayCategory.html",{'data':data})
def editcategory(request,dataid):
    data = CategoryDB.objects.get(id=dataid)
    return render(request, "EditCategory.html",{'data': data})

def updatecategory(request,dataid):
    if request.method=="POST":
        cn = request.POST.get('c_name')
        des = request.POST.get('c_description')
        try:
            img = request.FILES['c_img']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).Image
        CategoryDB.objects.filter(id=dataid).update(CategoryName=cn,Description=des,Image=file)
        messages.success(request, "Edited Successfully...")
        return redirect(displaycategory)

def deletecategory(request,dataid):
    data = CategoryDB.objects.filter(id=dataid)
    data.delete()
    messages.error(request, "Category deleted Successfully...")
    return redirect(displaycategory)
def addproduct(request):
    cat = CategoryDB.objects.all()
    return render(request,"AddProduct.html",{'cat':cat})
def savedata2(request):
    if request.method=="POST":
        cn = request.POST.get('p_cname')
        pn = request.POST.get('p_name')
        pq = request.POST.get('p_quantity')
        pr = request.POST.get('p_price')
        img = request.FILES['p_img']
        obj = ProductDB(CategoryName=cn,ProductName=pn,Quantity=pq,Price=pr,ProductImage=img)
        obj.save()
        return redirect(addproduct)
def displayproduct(request):
    data = ProductDB.objects.all()
    return render(request, "DisplayProduct.html", {'data': data})

def editproduct(request,dataid):
    cat = CategoryDB.objects.all()
    data = ProductDB.objects.get(id=dataid)
    return render(request,"EditProduct.html",{'cat':cat,'data':data})




def updateproduct(request,dataid):
    if request.method=="POST":
        cn = request.POST.get('p_cname')
        pn = request.POST.get('p_name')
        pq = request.POST.get('p_quantity')
        pr = request.POST.get('p_price')
        try:
            img = request.FILES['p_img']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=dataid).ProductImage
        ProductDB.objects.filter(id=dataid).update(CategoryName=cn,ProductName=pn,Quantity=pq,Price=pr,ProductImage=file)
        return redirect(displayproduct)



def deleteproduct(request,dataid):
    data = ProductDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def adminlogin(request):
    return render(request,"Adminlogin.html")

def adminlogpage(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        psd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname,password=psd)
            if user is not None:
                login(request,user)
                request.session['username'] = uname
                request.session['password'] = psd
                messages.success(request, "Login Successfully...")
                return redirect(indexpage)
            else:
                messages.error(request, "Sorry...check Username/password")
                return redirect(adminlogin)
        else:
            messages.error(request, "Sorry...check Username/password")
            return redirect(adminlogin)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Loginout Successfully...")
    return redirect(adminlogin)