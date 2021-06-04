from django.shortcuts import render
#from django.shortcuts import render
from django.core.mail import send_mail


#from django.http import HttpResponse
#from django.conf import settings

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
            ['ayaoshima0221@gmail.com'],
            fail_silently=False
        )

    return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})

'''
# --------------------------------------------------------------------------------


def home(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        note = request.POST['note']

        send_mail(
            'お問い合わせ' + name + '様',
            subject + note + phone,
            email,
            # phone,
            # subject,
            ['isono@isono-law.com'],
            fail_silently=False
        )

        return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})
    # return render(request, 'contact.html', {'name': name})

    # else:
    # return render(request, 'contact.html', {})


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
