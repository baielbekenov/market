from django.contrib import admin

from market.models import Good, Goods, CounterParty, Measurement, VhodOstatok, ObrabotkaPrihod, ObrabotkaRashod, \
    IshodRashod

admin.site.register(Good)
admin.site.register(Goods)
admin.site.register(CounterParty)
admin.site.register(Measurement)
admin.site.register(VhodOstatok)
admin.site.register(ObrabotkaPrihod)
admin.site.register(ObrabotkaRashod)
admin.site.register(IshodRashod)