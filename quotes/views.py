from django.shortcuts import render
from .models import Quotes
from random import choice

def home(request):
    quotes = Quotes.objects.all()
    quote = choice(quotes) if quotes else None
    return render(request, 'home.html', {'quote': quote})