from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from . import forms

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(request, "users/register.html",{
            "form": forms.CustomUserCreationForm()})
    elif request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))