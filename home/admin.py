from django.contrib import admin
from django.contrib.auth.models import Group, User
from solo.admin import SingletonModelAdmin

from .models import (AboutMeBlock, BlockFlatRoof, BlockSlopRoof, InfoCompany,
                     MainBlock, Metrics, Portfolio, ProfitBlock, Seo,
                     WorkPriceImage)

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(InfoCompany, SingletonModelAdmin)
admin.site.register(MainBlock, SingletonModelAdmin)
admin.site.register(ProfitBlock, SingletonModelAdmin)
admin.site.register(AboutMeBlock, SingletonModelAdmin)

admin.site.register(Seo, SingletonModelAdmin)
admin.site.register(Metrics, SingletonModelAdmin)

admin.site.register(Portfolio)


class WorkPriceImageInline(admin.TabularInline):
    model = WorkPriceImage

    fields = (
        'work', 'price', 'image'
    )


@admin.register(BlockFlatRoof)
class BlockFlatRoofAdmin(SingletonModelAdmin):
    inlines = [
        WorkPriceImageInline,
    ]


@admin.register(BlockSlopRoof)
class BlockSlopRoofAdmin(SingletonModelAdmin):
    inlines = [
        WorkPriceImageInline,
    ]
