from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib import messages
from .models import user_accounts
from django.views import View
from .forms import LoginForm


def accountsView(request):
    return render(request, "accounts/accounts.html")

def logout_view(request):
    logout(request)
    return redirect(loginView)

def loginView(request):
    if request.method == 'POST':

        next_url = request.POST.get('next')
        request.session['next_url'] = next_url

        # check the next url
        if not next_url:
            next_url = request.session.get('next_url')

        login_form = LoginForm(request, data=request.POST)
        
        if login_form.is_valid():
            email = request.POST.get('username')
            codeMelli = request.POST.get('codeMelli')
            password = request.POST.get('password')
            if (user_accounts.objects.filter(email = email, codeMelli = codeMelli)).exists():
                user = authenticate(request=request, username= email, codeMelli= codeMelli, password=password)
                login(request, user)
                if next_url:
                    del request.session['next_url']
                    return redirect(next_url)
                else:
                    return redirect('/')
            else:
                login_form = LoginForm()
                messages.success(request, 'Your success message here')
                return render(request, 'accounts/login.html', {'login': login_form,})
    else:
        login_form = LoginForm()
        return render(request, 'accounts/login.html', {'login': login_form,})