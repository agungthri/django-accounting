from django import forms
from . import models
from django.db.models import Q



class AccountFormAdd(forms.Form):

    select_account = forms.ModelChoiceField(
        queryset=models.Account.objects.all(),
        required=True,
        label='Masukkan Sub Account')
    sub_account_name = forms.CharField(
        max_length=50,
        required=True,
        label='Nama Sub Account')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('user', None)
        super(AccountFormAdd, self).__init__(*args, **kwargs)
        self.fields['select_account'].queryset = models.Account.objects.filter(
            Q(user="init") | Q(user=self.request)
            ).order_by("c1","c2","c3","c4","c5","c6")
   



class AccountFormDel(forms.Form):

    select_account = forms.ModelChoiceField(
        queryset=models.Account.objects.all(),
        required=True,
        label='Masukkan Sub Account')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('user', None)
        super(AccountFormDel, self).__init__(*args, **kwargs)
        self.fields['select_account'].queryset = models.Account.objects.filter(
            Q(user="init") | Q(user=self.request)
            ).order_by("c1","c2","c3","c4","c5","c6")
    


class Date(forms.Form):

    date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type':'date'}),
        label="Date")
    


class Desc(forms.Form):

    desc = forms.CharField(
        max_length=100,
        label="Description")



class Type(forms.Form):

    type = forms.CharField(
        max_length=100,
        label="Type")
    


class AccountFormDebit(forms.Form):
    
    account = forms.ModelChoiceField(
        queryset=models.Account.objects.all(),
        empty_label="",
        required=True,
        label="")
    amount = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            "onblur":"findTotalDebit()",
            "class":"sum-debit",
            "style":"text-align:right;",
            "placeholder":"Total Debit"}))
    pos = forms.CharField(widget=forms.HiddenInput(), initial="dr")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('user', None)
        super(AccountFormDebit, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = models.Account.objects.filter(
            Q(user="init") | Q(user=self.request)
            ).order_by("c1","c2","c3","c4","c5","c6")
    


class AccountFormCredit(forms.Form):
    account = forms.ModelChoiceField(
        queryset=models.Account.objects.all(),
        empty_label="",
        required=True,
        label='')
    amount = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            "onblur":"findTotalCredit()",
            "class":"sum-credit",
            "style":"text-align:right;",
            "placeholder":"Total Credit"}))
    pos = forms.CharField(widget=forms.HiddenInput(), initial="cr")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('user', None)
        super(AccountFormCredit, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = models.Account.objects.filter(
            Q(user="init") | Q(user=self.request)
            ).order_by("c1","c2","c3","c4","c5","c6")
    



