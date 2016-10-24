from tipsonapp.models import ToolsInfo
from django.shortcuts import render
from django.template import RequestContext
import json
from django.contrib.auth.decorators import login_required
from tipsonapp.models import ComUser
from django.http import HttpResponse

@login_required

def get_results(request):
    request_context = RequestContext(request)  
    if request.method=='POST':
        searchparam=request.POST
        val=searchparam.get('searchbar')
        print val
        toolsdata=get_tooldata(val)
	print toolsdata
        imagedata=get_imagedata(val)
        alltools=getAllTools()
        jsonstr=imagedata[0]
        imjsdata=jsonstr['imagelinks']
        res=json.loads(imjsdata)
        loggedUser=getUserData(request.user)
        return render(request,'searchresults.html', {'toolsdata':toolsdata,'alltools':alltools,'imagedata':res,'loggedUser':loggedUser})
    else:
        user=request.user
        print user
	if user==None:
            return render(request,'login.html',{'message':'You are not logged in! Please login or signup...'})
        else:
            return HttpResponse("No post data found ")

def get_tooldata(val):
    if val=='All Products':
        return getAllTools()
    
    return ToolsInfo.objects.filter(steel=val).order_by('steel').values()

def get_imagedata(val):
    if val=='All Products':
	return get_allImages()
    
    return ToolsInfo.objects.filter(steel=val).values('imagelinks')


def getAllTools():
   return ToolsInfo.objects.all().order_by('steel').values()

def getUserData(user):
    return ComUser.objects.filter(email=user).values()

def get_allImages():
    return ToolsInfo.objects.all().values('imagelinks')

