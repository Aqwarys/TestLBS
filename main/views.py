from django.shortcuts import render
from user.models import BankAccount
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='user:login')
def main(request):
    bankaccount = None
    if request.user.is_authenticated:
        bankaccount = BankAccount.objects.filter(owner=request.user).first()
    context = {
        'user': request.user,
        'bankaccount': bankaccount
    }
    return render(request, 'main/main.html', context=context)