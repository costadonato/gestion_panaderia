from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

@login_required (login_url='usuario:login')
def home(request):
    return render(request, "base/home.html")