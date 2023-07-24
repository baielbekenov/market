from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название товара')
    code_number = models.CharField(max_length=4, verbose_name='Код товара')

    def __str__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=30, verbose_name='Единица измерения')

    def __str__(self):
        return self.name


class Deliver(models.Model):
    name = models.CharField(max_length=50, verbose_name='Поставщик')

    def __str__(self):
        return self.name


class Goods(models.Model):
    date = models.DateField(auto_now_add=True)
    good_id = models.ForeignKey(Good, on_delete=models.SET_NULL, blank=True, null=True,
                                verbose_name='Наименование товара')
    measure_id = models.ForeignKey(Measure, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Единица измерение')
    deliver_id = models.ForeignKey(Deliver, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Поставщики')
    good_name = models.CharField(max_length=25)
    code_number = models.CharField(max_length=4)
    good_number = models.CharField(max_length=4, verbose_name='Номер товара')
    measure_name = models.CharField(max_length=30)
    amount = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')


    def __str__(self):
        return self.good_number


class Transactions(models.Model):
    TRANSACTION_TYPES = (
        ('Income', 'Income'),
        ('Outcome', 'Outcome'),
    )

    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
