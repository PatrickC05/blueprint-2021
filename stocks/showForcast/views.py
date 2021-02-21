from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import util

def index(request):
    return render(request, "home.html")

def get_prices(request, ticker):
    if ticker:
        l = [i/100 for i in range(37)]
        return JsonResponse({"prices":util.getPrices(ticker)})
    return JsonResponse({"error": "stock does not exist"},status=404)

def showStock(request, ticker):
    return render(request, "view.html", {'ticker': ticker})

def about(request):
    return render(request, "about.html")
