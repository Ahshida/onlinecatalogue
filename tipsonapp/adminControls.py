from tipsonapp.models import Enquiry
from tipsonapp.models import ComUser
from tipsonapp.models import ToolsInfo
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

def displayAllTables(request):
	request_context=RequestContext(request)
	userdata=ComUser.objects.all().values()
	toolsdata=ToolsInfo.objects.all().values()
	enquirydata=Enquiry.objects.all().values()
	return render(request,'adminDash.html')

def listData(request):
	val=''
	request_context = RequestContext(request)  
	if request.method=='POST':
		searchparam=request.POST
		val=searchparam.get('searchbar')
	if val=='Enquiry':
		data=Enquiry.objects.all().values()
	elif val=='User':
		data=ComUser.objects.all().values()
	else:
		data=ToolsInfo.objects.all().values()
	return render(request,'adminDash.html',{'data':data})
