from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi")

def get_prices(request, ticker):
    l = [i/100 for i in range(30)]
    return JsonResponse({"prices":l})
