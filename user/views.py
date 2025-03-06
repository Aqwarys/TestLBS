from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .form import UserRegestrationForm, UserLoginForm, SendMoneyForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from banksystem.models import Transactions

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
    next_page = reverse_lazy('user:login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect(reverse_lazy('main:main'))
    context = {
        'form': UserLoginForm
    }
    return render(request, 'user/login.html', context=context)


def send_money(request):
    if request.method == 'POST':
        form = SendMoneyForm(request.POST)
        if form.is_valid():
            receiver_card_number = form.cleaned_data['receiver_card_number']
            amount = form.cleaned_data['amount']
            comment = form.cleaned_data['comment']
            reveiver_user = BankAccount.objects.filter(card_number=receiver_card_number).first()
            if reveiver_user:
                reveiver_user.balance += amount
                reveiver_user.save()
                sender_user = BankAccount.objects.filter(owner=request.user).first()
                sender_user.balance -= amount
                sender_user.save()
                Transactions.objects.create(sender=sender_user, recipient=reveiver_user, amount=amount, comment=comment)
                return redirect(reverse_lazy('main:main'))
    context = {
        'form': SendMoneyForm
    }
    return render(request, 'user/send_money.html', context=context)