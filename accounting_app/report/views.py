from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from transaction import models

# Create your views here.

def report(request):
    return render(request, "report/report.html")

@login_required(login_url='login')
def report_laba_rugi(request):
    accounts = models.Account.objects.all().order_by("c1","c2","c3","c4",).filter(c1__gte=4)
    account_list = []
    default_pos_list = []
    default_pos_sum_list = []
    sum_all_dr = 0
    sum_all_cr = 0
    for account in accounts:
        data = account.journal_set.all()
        if data:
            default_pos  = account.dp
            total_sum_dr = data.filter(pos="dr").aggregate(Sum("total"))['total__sum'] or 0
            total_sum_cr = data.filter(pos="cr").aggregate(Sum("total"))['total__sum'] or 0
            if default_pos == 'dr':
                default_pos_sum_list.append(total_sum_dr - total_sum_cr)
                sum_all_dr += total_sum_dr - total_sum_cr
            if default_pos == 'cr':
                default_pos_sum_list.append(total_sum_cr - total_sum_dr)
                sum_all_cr += total_sum_cr - total_sum_dr
            default_pos_list.append(default_pos)
            account_list.append(account)
    return render(request, "report/report_laba_rugi.html", {
        "datas":zip(account_list, default_pos_list, default_pos_sum_list),
        "sum_all_dr":sum_all_dr,
        "sum_all_cr":sum_all_cr,

    })


@login_required(login_url='login')
def report_neraca(request):
    accounts = models.Account.objects.all().order_by("c1","c2","c3","c4",).filter(c1__lte=3)
    account_list = []
    default_pos_list = []
    default_pos_sum_list = []
    sum_all_dr = 0
    sum_all_cr = 0
    for account in accounts:
        data = account.journal_set.all()
        if data:
            default_pos  = account.dp
            total_sum_dr = data.filter(pos="dr").aggregate(Sum("total"))['total__sum'] or 0
            total_sum_cr = data.filter(pos="cr").aggregate(Sum("total"))['total__sum'] or 0
            if default_pos == 'dr':
                default_pos_sum_list.append(total_sum_dr - total_sum_cr)
                sum_all_dr += total_sum_dr - total_sum_cr
            if default_pos == 'cr':
                default_pos_sum_list.append(total_sum_cr - total_sum_dr)
                sum_all_cr += total_sum_cr - total_sum_dr
            default_pos_list.append(default_pos)
            account_list.append(account)
    return render(request, "report/report_neraca.html", {
        "datas":zip(account_list, default_pos_list, default_pos_sum_list),
        "sum_all_dr":sum_all_dr,
        "sum_all_cr":sum_all_cr,

    })


@login_required(login_url='login')
def report_neraca_saldo(request):
    accounts = models.Account.objects.all().order_by("c1","c2","c3","c4",)
    account_list = []
    default_pos_list = []
    default_pos_sum_list = []
    sum_all_dr = 0
    sum_all_cr = 0
    for account in accounts:
        data = account.journal_set.all()
        if data:
            default_pos  = account.dp
            total_sum_dr = data.filter(pos="dr").aggregate(Sum("total"))['total__sum'] or 0
            total_sum_cr = data.filter(pos="cr").aggregate(Sum("total"))['total__sum'] or 0
            if default_pos == 'dr':
                default_pos_sum_list.append(total_sum_dr - total_sum_cr)
                sum_all_dr += total_sum_dr - total_sum_cr
            if default_pos == 'cr':
                default_pos_sum_list.append(total_sum_cr - total_sum_dr)
                sum_all_cr += total_sum_cr - total_sum_dr
            default_pos_list.append(default_pos)
            account_list.append(account)
    return render(request, "report/report_neraca_saldo.html", {
        "datas":zip(account_list, default_pos_list, default_pos_sum_list),
        "sum_all_dr":sum_all_dr,
        "sum_all_cr":sum_all_cr,

    })


@login_required(login_url='login')
def report_buku_besar(request):
    accounts = models.Account.objects.all().order_by("c1","c2","c3","c4",)
    data_list = []
    default_pos_list = []
    default_pos_sum_list = []
    account_list = []
    total_sum_all_dr = 0
    total_sum_all_cr = 0
    for account in accounts:
        data = account.journal_set.all()
        if data:
            default_pos  = account.dp
            total_sum_dr = data.filter(pos="dr").aggregate(Sum("total"))['total__sum'] or 0
            total_sum_cr = data.filter(pos="cr").aggregate(Sum("total"))['total__sum'] or 0
            if default_pos == 'dr':
                default_pos_sum_list.append(total_sum_dr - total_sum_cr) 
            if default_pos == 'cr':
                default_pos_sum_list.append(total_sum_cr - total_sum_dr)
            default_pos_list.append(default_pos)
            data_list.append(data)
            account_list.append(account)
            total_sum_all_dr += total_sum_dr
            total_sum_all_cr += total_sum_cr
    return render(request, "report/report_buku_besar.html", {
        "datas":zip(data_list, default_pos_list, default_pos_sum_list, account_list),
        "total_sum_all_dr":total_sum_all_dr,
        "total_sum_all_cr":total_sum_all_cr,
    })
