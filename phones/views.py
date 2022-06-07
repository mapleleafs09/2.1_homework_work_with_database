from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_map = { 'max_price':'-price', 'min_price':'price', 'name':'name'}
    sort = request.GET.get('sort')
    phones = Phone.objects.all().order_by(sort_map.get(sort, 'id'))
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone' : phone}
    return render(request, template, context)
