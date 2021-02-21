from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.templatetags.static import static
stocks = []

with open(static("symbol_list.txt")) as f:
    pass

def index(request):
    return HttpResponse("Hello")

def get_prices(request, ticker):
    print(stocks[:10])
    if ticker in stocks:
        l = [i/100 for i in range(30)]
        return JsonResponse({"prices":l})
    return JsonResponse({"error": "stock does not exist"},status=404)
