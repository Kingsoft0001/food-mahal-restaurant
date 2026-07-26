from django.shortcuts import render
from .models import *
from datetime import date

# Create your views here.

def index(request):
    cdata=tblcategory.objects.all().order_by("-id")[0:4]
    tdata=tblteam.objects.all().order_by("-id")
    pdata=tblproduct.objects.all().order_by("-discounted_price")[0:3]
    md={"cdata":cdata,"tdata":tdata,"products":pdata}
    return render(request,"user/index.html",md)

def about(request):
    return render(request,"user/about.html")

def contact(request):
    md={}
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("mobile")
        c=request.POST.get("email")
        d=request.POST.get("msg")
        tblcontact(name=a,mobile=b,email=c,message=d).save()
        md={"msg":"Data Saved Successfully..."}

    return render (request,"user/contact.html",md)

def gallery(request):
    data=tblgallery.objects.all().order_by("-id")
    md={"rows":data}
    return render(request,"user/gallery.html",md)

def team(request):
    data=tblteam.objects.all().order_by("-id")
    md={"tdata":data}
    return render(request,"user/team.html",md)

def booking(request):
    md={}
    if request.method=="POST":
        nop=request.POST.get("nop")
        amount=request.POST.get("amount")
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        bookdate=request.POST.get("date")
        time=request.POST.get("time")
        message=request.POST.get("msg")
        address=request.POST.get("address")
        tbl_booking(customer_name=name,mobile=mobile,email=email,no_of_people=nop,amount=amount,message=message,date=bookdate,time=time,address=address,booking_date=date.today()).save()
        md={"msg":"Table booked successfully! Your reservation request has been received."}
    return render(request,"user/booking.html",md)

def offers(request):
    pdata=tblproduct.objects.all().order_by("-discounted_price")
    md={"products":pdata}    
    return render(request,"user/offers.html",md)
def menu(request):
    cid=request.GET.get("msg")
    pdata=""
    if cid is not None:
        pdata=tblproduct.objects.all().filter(category=cid)
    else: 
        pdata=tblproduct.objects.all()    
    cdata=tblcategory.objects.all().order_by("-id")
    md={"cdata":cdata,"products":pdata}
    return render(request,"user/menu.html",md)

def developer(request):
    return render(request,"user/developer.html")

