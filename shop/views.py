from django.shortcuts import render
from shop.models import Clothes


def clothes_list(request):
    search = request.GET.get('search')

    if search:
        clothes_list = Clothes.objects.filter(name__icontains=search)
    else:
        clothes_list = Clothes.objects.all()

    return render(request, 'Clothes/clothes_list.html', {
        'clothes_list': clothes_list
    })