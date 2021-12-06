from django import http
from django.shortcuts import redirect, render

from .forms import CryptoCurrencyInfoForm
from .models import CryptoCurrencyInfo

def index(request):
    return render(request, 'BuyOrSell/about.html')

def add_crypto_info(request):
    error = ''
    form = CryptoCurrencyInfoForm
    if request.method == 'POST':
        form = CryptoCurrencyInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error = "There was an error in form"
    context = {
        'form' : form,
        'error': error
    }
    return render(request, 'BuyOrSell/addInfoAboutCrypto.html', context)

def explore_crypto(request):
    cryptos = CryptoCurrencyInfo.objects.order_by('name')
    return render(request, 'BuyOrSell/exploreCrypto.html', {'title' : 'Browse crypto', 'cryptos': cryptos})