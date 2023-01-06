from django import forms
from . import models



class AccountFormAdd(forms.Form):
    select_account = forms.ModelChoiceField(
        queryset=models.Account.objects.all().order_by("c1","c2","c3","c4","c5","c6"),
        required=True,
        label='Masukkan Sub Account')
    sub_account_name = forms.CharField(
        max_length=50,
        required=True,
        label='Nama Sub Account')



class AccountFormDel(forms.Form):
    select_account = forms.ModelChoiceField(
        queryset=models.Account.objects.all().order_by("c1","c2","c3","c4","c5","c6"),
        required=True,
        label='Masukkan Sub Account')
    


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
        queryset=models.Account.objects.all().order_by("c1","c2","c3","c4","c5","c6"),
        required=True,
        label='Dr')
    amount = forms.IntegerField(
        label="Total",
        widget=forms.NumberInput(attrs={
            "onblur":"findTotalDebit()",
            "class":"sum-debit"}))
    pos = forms.CharField(widget=forms.HiddenInput(), initial="dr")
    


class AccountFormCredit(forms.Form):
    account = forms.ModelChoiceField(
        queryset=models.Account.objects.all().order_by("c1","c2","c3","c4","c5","c6"),
        required=True,
        label='Cr')
    amount = forms.IntegerField(
        label="Total",
        widget=forms.NumberInput(attrs={
            "onblur":"findTotalCredit()",
            "class":"sum-credit"}))
    pos = forms.CharField(widget=forms.HiddenInput(), initial="cr")
    



