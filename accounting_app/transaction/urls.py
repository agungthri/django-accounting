from django.urls import path

from . import views

urlpatterns = [
    path('', views.transaction, name='transaction'),

    #transaction field
    path('add_transaction/',          views.add_transaction, name='add_transaction'),
    path('det_transaction/<int:pk>/', views.det_transaction, name='det_transaction'),
    path('edt_transaction/<int:pk>/', views.edt_transaction, name='edt_transaction'),
    path('del_transaction/<int:pk>/', views.del_transaction, name='del_transaction'),

    #account field
    path('add_account/', views.add_account, name='add_account'),
    path('del_account/', views.del_account, name='del_account'),
    path('all_account/', views.all_account, name='all_account'),

    #report
    path('report_buku_besar/', views.report_buku_besar, name='report_buku_besar'),
    path('report_neraca_saldo/', views.report_neraca_saldo, name='report_neraca_saldo'),
    path('report_neraca/', views.report_neraca, name='report_neraca'),
    path('report_laba_rugi/', views.report_laba_rugi, name='report_laba_rugi'),
    
]