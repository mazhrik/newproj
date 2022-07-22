from django.contrib import auth, messages

from django.shortcuts import render
from django.core.mail import send_mail

from website.models import tablee
from validate_email import validate_email
import pyautogui


def home(request):
    return render(request, "index.html")


def appointment(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        select_time = request.POST['select_time']
        phone = request.POST['phone']
        message = request.POST['message']
        check = validate_email(email, verify=True)
        if (check == True):
            send_mail(
                'New Appointment from ' + name + " on " + date,
                message,
                email,
                ['malikmuneeb98900@gmail.com ']
            )
            ins = tablee(name=name, email=email, phone=phone)
            ins.save()
            messages.success(request, 'Successful Appointment ')
            return render(request, 'appointment.html', {
                'name': name,
                'email': email,
                'date': date,
                'select_time': select_time,
                'phone': phone,
                'message': message,

            })
        else:
            messages.error(request, 'Invalid Email; Renter Email')
            return render(request, 'index.html')


    else:
        return render(request, 'index.html')


def page2(request):
    return render(request, "newpage.html")

def page3(request):
    return render(request, "lens.html")
