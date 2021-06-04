from django.urls import include, path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('legal_topics/', views.LegalTopicsView.as_view(), name='legal_topics'),
    path('domestic_law/', views.DomesticLawView.as_view(), name='domestic_law'),
    path('family_law/', views.FamilyLawView.as_view(), name='family_law'),
    path('money_law/', views.MoneyLawView.as_view(), name='money_law'),
    path('work_law/', views.WorkLawView.as_view(), name='work_law'),
    path('dailylife_law/', views.DailylifeLawView.as_view(), name='dailylife_law'),
    path('price/', views.PriceView.as_view(), name='price'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('404/', views.ErrorView.as_view(), name='404'),

]


