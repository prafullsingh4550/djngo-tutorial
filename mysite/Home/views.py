from django.shortcuts import render , HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    messages.success(request, 'This is a a test messgae !!' )
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")
    # return HttpResponse("this is about page")

def contact(request):
    
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        des = request.POST.get('des')
        contact = Contact(name= name, email= email , phone= phone, des= des,date= datetime.today())
        contact.save()
        messages.success(request, 'Your Message is Successfully Sent !!' )
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")
    
