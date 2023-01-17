from django.urls import path

from . import views

urlpatterns = [
    
    #report
    path('', views.report, name="report"),
    
    path('report_buku_besar/', views.report_buku_besar, name='report_buku_besar'),
    path('report_neraca_saldo/', views.report_neraca_saldo, name='report_neraca_saldo'),
    path('report_neraca/', views.report_neraca, name='report_neraca'),
    path('report_laba_rugi/', views.report_laba_rugi, name='report_laba_rugi'),
    path('report_perubahan_modal/', views.report_perubahan_modal, name='report_perubahan_modal'),
    
]