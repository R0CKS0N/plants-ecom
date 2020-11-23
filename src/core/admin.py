from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Item, OrderItem, Order



def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    ]
    list_display_links = [
        'user',
    ]
    list_filter = ['ordered',
    ]
    search_fields = [
        'user__username',
    ]
    actions = [make_refund_accepted]



@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    pass

admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
