from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from . import models
from . import forms



# Create your views here.

@login_required(login_url='login')
def transaction(request):
    data_transaction = models.Transaction.objects.all()
    return render(request, 'transaction/transaction.html', {
        'data_transaction':data_transaction,})


@login_required(login_url='login')
def add_transaction(request):
    if request.POST:
        account = request.POST.getlist('account')
        pos = request.POST.getlist('pos')
        total = request.POST.getlist('amount')
        transaction = models.Transaction.objects.create(
            date=request.POST.getlist('date')[0],
            type=request.POST.getlist('type')[0],
            desc=request.POST.getlist('desc')[0])
        account_dict = {i.pk:i for i in models.Account.objects.filter(pk__in=account)}
        obj_list = []
        for i in zip(account, pos, total):
            obj_list.append(
                models.Journal(
                    account=account_dict[int(i[0])],
                    transaction=transaction,
                    pos=i[1],
                    total=i[2]))
        models.Journal.objects.bulk_create(obj_list)
    return render(request, 'transaction/add_transaction.html', {
        'date':forms.Date(),
        'type':forms.Type(),
        'desc':forms.Desc(),
        'form_debit':forms.AccountFormDebit(),
        'form_credit':forms.AccountFormCredit(),})


@login_required(login_url='login')
def det_transaction(request, pk):
    transaction = models.Transaction.objects.get(pk=pk)
    return render(request, "transaction/det_transaction.html", {
        "data":transaction.journal_set.all()
        })


@login_required(login_url='login')
def edt_transaction(request, pk):
    transaction = models.Transaction.objects.get(id=pk)
    journal = transaction.journal_set.all()
    account_form_debit = []
    account_form_credit = []
    for i in journal:
        if i.pos == 'dr':
            account_form_debit.append(
                forms.AccountFormDebit(
                    initial={
                        'account':i.account,
                        'pos':i.pos,
                        'amount':i.total}))
        if i.pos == 'cr':
            account_form_credit.append(
                forms.AccountFormCredit(
                    initial={
                        'account':i.account,
                        'pos':i.pos,
                        'amount':i.total}))
    if request.POST:
        account = request.POST.getlist('account')
        pos = request.POST.getlist('pos')
        total = request.POST.getlist('amount')
        transaction.date=request.POST.getlist('date')[0]
        transaction.type=request.POST.getlist('type')[0]
        transaction.desc=request.POST.getlist('desc')[0]
        transaction.save()
        account_dict = {i.pk:i for i in models.Account.objects.filter(pk__in=account)}
        obj_all = []
        for new in zip(journal, account, pos, total):
            instance = new[0]
            instance.account = account_dict[int(new[1])] 
            instance.pos = new[2]
            instance.total = new[3]
            obj_all.append(instance)
        models.Journal.objects.bulk_update(obj_all, fields=['account', 'pos', 'total'])
        return HttpResponseRedirect(reverse('transaction'))      
    return render(request, "transaction/edt_transaction.html", {
        'date':forms.Date({'date':transaction.date}),
        'type':forms.Type({'type':transaction.type}),
        'desc':forms.Desc({'desc':transaction.desc}),
        'account_form_debit':account_form_debit,
        'account_form_credit':account_form_credit,})


@login_required(login_url='login')
def del_transaction(request, pk):
    models.Transaction.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('transaction'))


@login_required(login_url='login')
def add_account(request):
    if request.POST:
        account_id = request.POST['select_account']
        sub_account = request.POST['sub_account_name']
        account = models.Account.objects.get(pk=account_id)
        code_list = {
            "c1":account.c1,
            "c2":account.c2,
            "c3":account.c3,
            "c4":account.c4,
            "c5":account.c5,
            "c6":account.c6}
        filter = {}
        index = 1
        for key, value in code_list.items():
            if value != 0:
                filter[key] = value
                index += 1
        result = models.Account.objects.filter(**filter)
        max_value = max(list(result.values_list(f"c{index}", flat=True)))
        code_list[f"c{index}"] = max_value + 1
        code_list['account'] = account.account + " / " + sub_account
        code_list['dp'] = account.dp
        models.Account.objects.create(**code_list)
    return render(request, 'transaction/add_account.html', {
        'form':forms.AccountFormAdd()})


@login_required(login_url='login')
def all_account(request):
    accounts = models.Account.objects.all().order_by("c1","c2","c3","c4","c5",)
    return render(request, "transaction/all_account.html", {
        "accounts":accounts
    })


@login_required(login_url='login')
def del_account(request):
    if request.POST:
        account_id = request.POST['select_account']
        if int(account_id) > 92:
            models.Account.objects.get(id=account_id).delete()
    return render(request, "transaction/del_account.html", {
        "form":forms.AccountFormDel()
    })


#Kas 10.000
    #Utang 10.000
