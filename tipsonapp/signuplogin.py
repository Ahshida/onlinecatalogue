from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from tipsonapp.models import ComUser
from tipsonapp.models import ToolsInfo
from tipsonapp import adminControls

from django.core.mail import EmailMessage
def errorpage(request):
    return render(request, 'errorpage.html')


def usersignup(request):
    if request.method == 'POST':

        request_context = RequestContext(request)
        username = request.POST['username']
        password = request.POST['password']

        email=request.POST['email']
        postalcode=request.POST['postalcode']
        contactnum=request.POST['contact']
        company=request.POST['company']
        address=request.POST['address']

        user=User.objects.create_user(email, email, password)
        newUser=ComUser(name=username,email=email,postcode=postalcode,address=address,contact=contactnum,company=company);
        newUser.save();
        return render(request,'login.html')




def authenticateUser(request):
    if request.method == 'POST':
       request_context = RequestContext(request)
       email = request.POST.get('email',False)
       logpassword = request.POST.get('password',False)
       user=None
       user = authenticate(username=email,password=logpassword)

    if user is not None:
    # the password verified for the user
       if user.is_active:
           login(request,user)
           loggedUser=ComUser.objects.filter(email=email).values()
           toolsdata=ToolsInfo.objects.all().order_by('steel').values()
           #ms.send_mail('User Created',loggedUser['name']+'is a new user to the system','sambhavk@hotmail.com','sambhavk11@gmail.com')
           #email = EmailMessage('Hello', 'World', to=['kssam12online@gmail.com'])
           #email.send()

           if email=='admin@tipson.com':

               return adminControls.displayAllTables(request)
           else:
                return render(request,'index.html', {'userdata': loggedUser,'toolsdata':toolsdata})
       else:
           return HttpResponse("User Inactive")
    else:
    # the authentication system was unable to verify the username and password
        return HttpResponse("User Cannot be Authenticated. Check Username or password")
