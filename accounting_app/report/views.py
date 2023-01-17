from django.shortcuts import render
from django.db.models import Sum, Q, Case, F, When, Count
from django.contrib.auth.decorators import login_required
from transaction import models
from datetime import datetime

# Create your views here.

def report(request):
    return render(request, "report/report.html")



def report_perubahan_modal(request):
    c1 = Q(account__user=request.user)
    c2 = Q(account__user="init")
    c3 = Q(journal__isnull=False)
    c4 = Q(user=request.user)
    c5 = Q(user="init")
    c6 = Q(c1=3)
    journal = models.Journal.objects.filter(c1 | c2).filter(account__c1=3)
    account_list = models.Account.objects.filter( c4 | c5 ).filter(c3).filter(c6).distinct()
    total_account = journal.values("account__account").annotate(
        dp=F("account__dp"),
        total=Case(
            When(account__dp='dr',then=Sum(Case(When(pos="dr",then=F("total")),default=0))-Sum(Case(When(pos="cr",then=F("total")),default=0))),
            When(account__dp='cr',then=Sum(Case(When(pos="cr",then=F("total")),default=0))-Sum(Case(When(pos="dr",then=F("total")),default=0))),
            ),
        ).order_by("account")
    dr=total_account.aggregate(dr=Sum(Case(When(dp='dr', then=F('total')), default=0)))
    cr=total_account.aggregate(cr=Sum(Case(When(dp='cr', then=F('total')), default=0)))
    return render(request, "report/report_perubahan_modal.html", {
        "data":zip(account_list, total_account),
        "dr":dr,
        "cr":cr,
    })



@login_required(login_url='login')
def report_laba_rugi(request):
    c1 = Q(account__user=request.user)
    c2 = Q(account__user="init")
    c3 = Q(journal__isnull=False)
    c4 = Q(user=request.user)
    c5 = Q(user="init")
    c6 = Q(c1__gte=4)
    journal = models.Journal.objects.filter(c1 | c2).filter(account__c1__gte=4)
    account_list = models.Account.objects.filter( c4 | c5 ).filter(c3).filter(c6).distinct()
    total_account = journal.values("account__account").annotate(
        dp=F("account__dp"),
        total=Case(
            When(account__dp='dr',then=Sum(Case(When(pos="dr",then=F("total")),default=0))-Sum(Case(When(pos="cr",then=F("total")),default=0))),
            When(account__dp='cr',then=Sum(Case(When(pos="cr",then=F("total")),default=0))-Sum(Case(When(pos="dr",then=F("total")),default=0))),
            ),
        ).order_by("account")
    dr=total_account.aggregate(dr=Sum(Case(When(dp='dr', then=F('total')), default=0)))
    cr=total_account.aggregate(cr=Sum(Case(When(dp='cr', then=F('total')), default=0)))
    return render(request, "report/report_laba_rugi.html", {
        "data":zip(account_list, total_account),
        "dr":dr,
        "cr":cr,
    })



@login_required(login_url='login')
def report_neraca(request):
    c1 = Q(account__user=request.user)
    c2 = Q(account__user="init")
    c3 = Q(journal__isnull=False)
    c4 = Q(user=request.user)
    c5 = Q(user="init")
    c6 = Q(c1__lte=3)
    journal = models.Journal.objects.filter(c1 | c2).filter(account__c1__lte=3)
    account_list = models.Account.objects.filter( c4 | c5 ).filter(c3).filter(c6).distinct()
    total_account = journal.values("account__account").annotate(
        dp=F("account__dp"),
        total=Case(
            When(account__dp='dr',then=Sum(Case(When(pos="dr",then=F("total")),default=0))-Sum(Case(When(pos="cr",then=F("total")),default=0))),
            When(account__dp='cr',then=Sum(Case(When(pos="cr",then=F("total")),default=0))-Sum(Case(When(pos="dr",then=F("total")),default=0))),
            ),
        ).order_by("account")
    dr=total_account.aggregate(dr=Sum(Case(When(dp='dr', then=F('total')), default=0)))
    cr=total_account.aggregate(cr=Sum(Case(When(dp='cr', then=F('total')), default=0)))
    return render(request, "report/report_neraca.html", {
        "data":zip(account_list, total_account),
        "dr":dr,
        "cr":cr,
    })



@login_required(login_url='login')
def report_neraca_saldo(request):
    c1 = Q(account__user=request.user)
    c2 = Q(account__user="init")
    c3 = Q(journal__isnull=False)
    c4 = Q(user=request.user)
    c5 = Q(user="init")
    journal = models.Journal.objects.filter(c1 | c2)
    account_list = models.Account.objects.filter( c4 | c5 ).filter(c3).distinct()
    total_account = journal.values("account__account").annotate(
        dp=F("account__dp"),
        total=Case(
            When(account__dp='dr',then=Sum(Case(When(pos="dr",then=F("total")),default=0))-Sum(Case(When(pos="cr",then=F("total")),default=0))),
            When(account__dp='cr',then=Sum(Case(When(pos="cr",then=F("total")),default=0))-Sum(Case(When(pos="dr",then=F("total")),default=0))),
            ),
        ).order_by("account")
    dr=total_account.aggregate(dr=Sum(Case(When(dp='dr', then=F('total')), default=0)))
    cr=total_account.aggregate(cr=Sum(Case(When(dp='cr', then=F('total')), default=0)))
    return render(request, "report/report_neraca_saldo.html", {
        "data":zip(account_list, total_account),
        "dr":dr,
        "cr":cr
        })



@login_required(login_url='login')
def report_buku_besar(request):
    c1 = Q(account__user=request.user)
    c2 = Q(account__user="init")
    c3 = Q(journal__isnull=False)
    c4 = Q(user=request.user)
    c5 = Q(user="init")
    journal = models.Journal.objects.filter(c1 | c2)
    account_list = models.Account.objects.filter( c4 | c5 ).filter(c3).distinct()
    total_account = journal.values("account__account").annotate(
        dp=F("account__dp"),
        total=Case(
            When(account__dp='dr',then=Sum(Case(When(pos="dr", then=F("total")), default=0 )) - Sum(Case(When(pos="cr", then=F("total")), default=0 ))),
            When(account__dp='cr',then=Sum(Case(When(pos="cr", then=F("total")), default=0 )) - Sum(Case(When(pos="dr", then=F("total")), default=0 ))),
            ),
        ).order_by("account")
    total = journal.values("pos").annotate(Sum("total"))
    return render(request, "report/report_buku_besar.html", {
        "data":zip(account_list, total_account),
        "total":total
    })
