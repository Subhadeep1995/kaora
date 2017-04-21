from django.shortcuts import render, redirect
from django.contrib.auth import logout

def profile(request):
    return redirect('questions')

def logout_view(request):
    logout(request)
    return redirect('questions')


