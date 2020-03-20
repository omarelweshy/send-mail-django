from django.shortcuts import render
from django.core.mail import send_mail
from . import forms
from SendEmail.settings import EMAIL_HOST_USER

def Sending(request):
    con = forms.Send()
    if request.method == 'POST':
        con = forms.Send(request.POST)
        subject = 'Welcome To Django Sending App'
        message = 'Welcome to our App, Have fun :)'
        recepient = str(con['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        context = {
            'recepient': recepient
        }
        return render(request, 'success.html', context)
    return render(request, 'home.html', {'form': con})