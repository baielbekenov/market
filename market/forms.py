from django.forms import ModelForm
from django import forms

from market.models import Goods, Good, Measure, Deliver


class GoodsForm(ModelForm):

    class Meta:
        model = Goods
        fields = ['good_id', 'measure_id', 'deliver_id', 'good_number', 'amount', 'price']


class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = '__all__'


class MeasureForm(ModelForm):
    class Meta:
        model = Measure
        fields = '__all__'


class DeliverForm(ModelForm):
    class Meta:
        model = Deliver
        fields = '__all__'



