'''
1.Django Mail Setup:

Sending email using Django is pretty easy and require less configuration.
In this tutorial, we will send email to provided email.

For this purpose, we will use Google's SMTP and a Gmail account to set sender.

Django provides built-in mail library django.core.mail to send email.

Before sending email, we need to make some changes in Gmail account because
for security reasons Google does not allow direct access (login) by any application.
So, login to the Gmail account and follow the urls.
It will redirect to the Gmail account settings where we need to allow
less secure apps but toggle the button.

https://myaccount.google.com/lesssecureapps

After that follow this url that is a additional security check to verify
the make security constraint.

https://accounts.google.com/DisplayUnlockCaptcha
Click on continue and all is setup.

2.Django Configuration:

Provide the smtp and Gmail account details into the settings.py file. For example

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'irfan.iit003@gmail.com'
EMAIL_HOST_PASSWORD = '*********'

3.Import Mail Library:

from django.core.mail import send_mail
Now, write a view function that uses built-in mail function to send mail. See the example

4.Django Email Example:

This example contains the following files.

// views.py

from django.http import HttpResponse
from djangpapp import settings
from django.core.mail import send_mail


def mail(request):
    subject = "Greetings"
    msg     = "Congratulations for your success"
    to      = "irfan.sssit@gmail.com"
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)

// urls.py

Put following url into urls.py file.

path('mail',views.mail)

Run Server and access it at browser

Here, the both email ids are mine, so I can verify the email by login to the account.

And after login, here we go!! I got the mail.
Well, same like, we can send mail using other smtp server configurations if we have.

'''