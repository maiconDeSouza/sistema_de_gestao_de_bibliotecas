from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class Login(View):
    def get(self, request):
        forms = AuthenticationForm()

        return render(request, 'account/pages/login.html', {"forms": forms})

    def post(self, request):
        login_user = AuthenticationForm(request, data=request.POST)

        if login_user.is_valid():
            user = login_user.get_user()
            login(request, user)
            return redirect('index')

        return render(request, 'account/pages/login.html', {"forms": login_user})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')
