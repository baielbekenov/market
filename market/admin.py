from django.contrib import admin

from market.models import Goods, Transactions, Good, Measure, Deliver

admin.site.register(Goods)
admin.site.register(Transactions)
admin.site.register(Good)
admin.site.register(Measure)
admin.site.register(Deliver)



