from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from .forms import RegisterForm

def profile(request):
    return redirect('questions')

def logout_view(request):
    logout(request)
    return redirect('questions')

class UserFormView(View):
    form_class = RegisterForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user.save()
            return redirect('questions')