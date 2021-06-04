from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class LegalTopicsView(generic.TemplateView):
    template_name = 'legal_topics.html'


class DomesticLawView(generic.TemplateView):
    template_name = 'domestic_law.html'


class FamilyLawView(generic.TemplateView):
    template_name = 'family_law.html'


class MoneyLawView(generic.TemplateView):
    template_name = 'money_law.html'


class WorkLawView(generic.TemplateView):
    template_name = 'work_law.html'


class DailylifeLawView(generic.TemplateView):
    template_name = 'dailylife_law.html'


class PriceView(generic.TemplateView):
    template_name = 'price.html'


class FaqView(generic.TemplateView):
    template_name = 'faq.html'


class ErrorView(generic.TemplateView):
    template_name = '404.html'


