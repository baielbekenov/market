from django.forms import ModelForm
from django import forms

from market.models import ObrabotkaPrihod, Good, Goods, CounterParty, Measurement


class ObrabotkaPrihodForm(ModelForm):

    class Meta:
        model = ObrabotkaPrihod
        fields = '__all__'


class GoodForm(ModelForm):

    class Meta:
        model = Good
        fields = '__all__'


class GoodsForm(ModelForm):

    class Meta:
        model = Goods
        fields = '__all__'


class CounterPartyForm(ModelForm):

    class Meta:
        model = CounterParty
        fields = '__all__'


class MeasurementForm(ModelForm):

    class Meta:
        model = Measurement
        fields = '__all__'