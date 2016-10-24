from django.core.mail import send_mail

def sendmail(subject,Message,sentBy, receiveBy):
    send_mail(subject, Message,sentBy,receiveBy,fail_silently=True)
