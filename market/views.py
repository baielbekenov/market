from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F

from market.forms import GoodsForm, GoodForm, MeasureForm, DeliverForm
from .models import Goods, Good, Measure, Deliver


def index(request):
    goods = Goods.objects.all().order_by('-id')
    total_price = goods.aggregate(total_price=Sum('price'))['total_price'] or 0
    total_goods_count = Goods.objects.count()
    page = Goods.objects.all().distinct('name')
    context = {'goods': goods, 'total_price': total_price, 'total_goods_count': total_goods_count,
               'page': page}
    return render(request=request, template_name='index.html', context=context)

def code_number(request, code_number):
    goods = Goods.objects.filter(code_number=code_number)
    unique_goods = [good for i, good in enumerate(goods) if good.name not in [g.name for g in goods[:i]]]
    context = {'unique_goods': unique_goods}
    return render(request=request, template_name='code_number.html', context=context)




def create_goods(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            goods = form.save(commit=False)
            good = get_object_or_404(Good, id=goods.good_id_id)
            measure = get_object_or_404(Measure, id=goods.measure_id_id)
            goods.good_name = good.name
            goods.code_number = good.code_number
            goods.measure_name = measure.name

            form.save()
            return redirect('/')
    else:
        form = GoodsForm()

    context = {'form': form}
    return render(request, 'create_goods.html', context)


def create_good(request):
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = GoodForm()

    context = {'form': form}
    return render(request, 'create_good.html', context)


def create_measure(request):
    if request.method == 'POST':
        form = MeasureForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = MeasureForm()

    context = {'form': form}
    return render(request, 'create_measure.html', context)


def create_deliver(request):
    if request.method == 'POST':
        form = DeliverForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = DeliverForm()

    context = {'form': form}
    return render(request, 'create_deliver.html', context)


