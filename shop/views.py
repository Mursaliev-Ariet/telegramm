from django.shortcuts import render

from shop.models import Clothes


def clothes_list(request):
    clothe_list = Clothes.objects.all()
    return render(request, 'Clothes/clothes_list.html',{"clothes_list" : clothe_list})