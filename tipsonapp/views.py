from django.shortcuts import render

# Create your views here.



def callIndex(request):
    return render(request,"index.html")
def callsignup(request):
    return render(request,"signup.html")
def calllogin(request):
    return render(request,"login.html")
def callconfirmation(request):
    return render(request,"confirmation.html")
