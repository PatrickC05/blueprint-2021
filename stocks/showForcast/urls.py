from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("prices/<str:ticker>",views.get_prices,name="get_prices"),
    path("stock", views.showStock,name="view")
]
