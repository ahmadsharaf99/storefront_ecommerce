from django.core.mail import send_mail, EmailMessage,mail_admins, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        EmailMessage('subject', 'message', 'from@ahmadbuy.com', ['adeniyi@gmail.com', 'ahmad@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Ahmad'})
