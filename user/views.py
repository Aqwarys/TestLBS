from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .form import UserRegestrationForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User

from django.views.generic.edit import CreateView

from .models import BankAccount
# Create your views here.
class UserRegestrationView(CreateView):
    form_class = UserRegestrationForm
    template_name = "user/regestration.html"
    success_url = reverse_lazy('main:main')

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.object:

            BankAccount.objects.create(owner=self.object)

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = authenticate(self.request, email=email, password=password)

            if user is not None:
                login(self.request, user=user)

        return response

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('user:regestration')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect(reverse_lazy('main:main'))
    context = {
        'form': UserLoginForm
    }
    return render(request, 'user/login.html', context=context)