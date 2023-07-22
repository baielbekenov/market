from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Sum, F

from market.forms import ObrabotkaPrihodForm, GoodForm, GoodsForm, CounterPartyForm, MeasurementForm
from market.models import ObrabotkaPrihod, ObrabotkaRashod


def index(request):
    prihod = ObrabotkaPrihod.objects.all().annotate(total=Sum('amount')).order_by('-id')
    context = {'prihod': prihod}
    return render(request=request, template_name='index.html', context=context)


def prihod_to_rashod(request, id):
    try:
        prihod = ObrabotkaPrihod.objects.get(id=id)
        ObrabotkaRashod.objects.create(date=prihod.date, good_id=prihod.good_id, goods_id=prihod.goods_id,
                                                counterparty_id=prihod.counterparty_id, amount=prihod.amount,
                                                price_prod=prihod.price_prod, summa=prihod.summa,
                                                doc_number=prihod.doc_number, measure_id=prihod.measure_id)
        prihod.delete()
        return HttpResponse("Приход израсходован")
    except ObrabotkaPrihod.DoesNotExist:
        return HttpResponse("Объект не найден.")


def rashod(request):
    rashod = ObrabotkaRashod.objects.all()
    context = {'rashod': rashod}
    return render(request=request, template_name='rashod.html', context=context)


def create_prihod(request):
    if request.method == 'POST':
        form = ObrabotkaPrihodForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = ObrabotkaPrihodForm()

    context = {'form': form}
    return render(request, 'create_prihod.html', context)


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


def create_goods(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = GoodsForm()

    context = {'form': form}
    return render(request, 'create_goods.html', context)


def counterparty(request):
    if request.method == 'POST':
        form = CounterPartyForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = CounterPartyForm()

    context = {'form': form}
    return render(request, 'create_counterparty.html', context)


def create_measure(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = MeasurementForm()

    context = {'form': form}
    return render(request, 'create_measure.html', context)
