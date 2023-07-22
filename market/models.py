from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.name


class CounterParty(models.Model):
    name = models.CharField(max_length=250, verbose_name='Контрагенты')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    name = models.CharField(max_length=100, verbose_name='Единица измерения')

    def __str__(self):
        return self.name


class VhodOstatok(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    good_id = models.ForeignKey(Good, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Группа товаров')
    goods_id = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Товары')
    counterparty_id = models.ForeignKey(CounterParty, on_delete=models.SET_NULL,
                                        null=True, blank=True, verbose_name='Контрагенты')
    amount = models.IntegerField(verbose_name='Количество')
    price_uch = models.FloatField(verbose_name='Цена учетная')
    price_prod = models.FloatField(verbose_name='Цена продажная')
    summa = models.FloatField(verbose_name='Сумма')
    measure_id = models.ForeignKey(Measurement, on_delete=models.SET_NULL,
                                   null=True, blank=True, verbose_name='Единица измерения')

    def __str__(self):
        return self.goods_id


class ObrabotkaPrihod(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    good_id = models.ForeignKey(Good, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Группа товаров')
    goods_id = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Товары')
    counterparty_id = models.ForeignKey(CounterParty, on_delete=models.SET_NULL,
                                        null=True, blank=True, verbose_name='Контрагенты')
    amount = models.IntegerField(verbose_name='Количество')
    price_uch = models.FloatField(verbose_name='Цена учетная')
    price_prod = models.FloatField(verbose_name='Цена продажная')
    summa = models.FloatField(verbose_name='Сумма')
    doc_number = models.IntegerField(verbose_name='Номер документа')
    measure_id = models.ForeignKey(Measurement, on_delete=models.SET_NULL,
                                   null=True, blank=True, verbose_name='Единица измерения')

    def __str__(self):
        return str(self.goods_id)


class ObrabotkaRashod(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    good_id = models.ForeignKey(Good, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Группа товаров')
    goods_id = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Товары')
    counterparty_id = models.ForeignKey(CounterParty, on_delete=models.SET_NULL,
                                        null=True, blank=True, verbose_name='Контрагенты')
    amount = models.IntegerField(verbose_name='Количество')
    price_prod = models.FloatField(verbose_name='Цена продажная')
    summa = models.FloatField(verbose_name='Сумма')
    doc_number = models.IntegerField(verbose_name='Номер документа')
    measure_id = models.ForeignKey(Measurement, on_delete=models.SET_NULL,
                                   null=True, blank=True, verbose_name='Единица измерения')

    def __str__(self):
        return str(self.goods_id)


class IshodRashod(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    good_id = models.ForeignKey(Good, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Группа товаров')
    goods_id = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Товары')
    counterparty_id = models.ForeignKey(CounterParty, on_delete=models.SET_NULL,
                                        null=True, blank=True, verbose_name='Контрагенты')
    amount = models.IntegerField(verbose_name='Количество')
    price_uch = models.FloatField(verbose_name='Цена учетная')
    price_prod = models.FloatField(verbose_name='Цена продажная')
    summa = models.FloatField(verbose_name='Сумма')
    measure_id = models.ForeignKey(Measurement, on_delete=models.SET_NULL,
                                   null=True, blank=True, verbose_name='Единица измерения')

    def __str__(self):
        return self.goods_id

