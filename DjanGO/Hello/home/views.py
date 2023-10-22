from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        "variable1":"This Is My Sent",
        "variable2":"Ritesh Is My Sent",
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')
  

def services(request):
    return render(request, 'service.html')
    

def contact(request):
    if request.method == "POST":
     email = request.POST.get('email')
     password = request.POST.get('password')
     contact = Contact(email=email , password=password , date=datetime.today())

    return render(request, 'contact.html')
    