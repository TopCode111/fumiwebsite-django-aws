from django.shortcuts import render
from django.contrib import messages
#from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
#Mailchimp
import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
#Sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
#from django.http import HttpResponse
#from django.conf import settings

# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID
# ----------------------------------------------------------------------------
'''
class IndexView(request):
    template_name = 'index.html'


class ContactView(request):
    template_name = 'contact.html'
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']

        send_mail(
            'お問い合わせフォーム',
            name,
            email,
            # phone,
            # subject,
            [''],
            fail_silently=False
        )

    return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})

'''
# --------------------------------------------------------------------------------


def home(request):
    return render(request, 'index.html', {})

'''
# How to send mail via Mailchimp Transactional API
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        from_email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        note = request.POST['note']
        
        #send_mail(
        #    'お問い合わせ' + name + '様',
        #    subject + note + phone,
        #    email,           
        #    [settings.EMAIL_HOST_USER],
        #    fail_silently=False
        #)
        
        mailchimp = MailchimpTransactional.Client("_3IfzBLBRPaZIuNPOZhTxw")
        message = {            
            "text": note,
            "subject": subject,
            "from_email": from_email,
            "from_name": name,
            "to": [
                {
                "email": "",                
                "type": "to"
                }
            ]
        }
        #print(mailchimp)
        try:            
            response = mailchimp.messages.send({"message":message})
            print("API called successfully".format(response))
        except ApiClientError as error:
            print("An exception occurred".format(error.text))

        return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})
'''
#How to send mail via Sendgird   
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        from_email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        note = request.POST['note']

        message = Mail(
            from_email=from_email,
            to_emails=settings.EMAIL_HOST_USER,
            subject=subject,
            html_content=note
        )
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print("success")
            print(response)
        except Exception as e:
            print("error")
            print(e)
        return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})

# -------------------------------------------------------------------------------


'''
from django.shortcuts import render
from django.template.response import TemplateResponse

from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, View

from .forms import ContactForm


class ContactFormView(View):
    def post(self, request, *args, **kwargs):
        return TemplateResponse(request, 'templataes/contact.html')

    def get(self, request):
        return TemplateResponse(request, 'templataes/contact.html')
'''

'''
#djanagoのフォーム使う方法
class ContactFormView(FormView):
    template_name = 'templates/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'templates/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context
'''
