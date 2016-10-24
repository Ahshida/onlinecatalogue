from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import HttpResponse
from django.core.mail import EmailMessage
from tipsonapp.models import ComUser
from tipsonapp.models import Enquiry

def launchEnquiry(request):
    user=request.user
    userdata=ComUser.objects.filter(email=user).values()
    return render(request,'orderdetails.html',{'userdata':userdata})

def sendEnquiryMail(request):
    if request.method == 'POST':
	user=request.user
        userdata=ComUser.objects.filter(email=user).values()
        
        request_context = RequestContext(request)
        ordprod = request.POST['orderprod']
        leadtime = request.POST['leadtime']
        enquiry=Enquiry(who=str(user),orderText=ordprod,leadTime=leadtime)
	enquiry.save()
	enqdata=Enquiry.objects.filter(who=str(user)).order_by('-timeofEnquiry')[:1]
	finaltext=ordprod+"\n\n\n"+leadtime+"\n\n\n Sender: " + str(user)
        email=EmailMessage('New Order Enquiry',finaltext, to=['sales@tipson.com.sg'],cc=[ 'tipson@singnet.com.sg','kssam12online@gmail.com'])
        email.send()
        return render(request,'confirmation.html',{'enqdata':enqdata,'userdata':userdata})
