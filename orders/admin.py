from django.contrib import admin

from .models import Operation, Order


class CustomOrderAdmin(admin.ModelAdmin):
    model = Order
    search_fields = ('user', 'created_at')
    list_display = (
        'id', 'user', 'operation_type',
        'amount', 'currency', 'created_at',
        )

    list_display_links = ('id', 'user',)
    ordering = ('pk',)


class CustomOperationAdmin(admin.ModelAdmin):
    model = Operation
    list_display = (
        'id', 'order_id', 'order', 'operator',
        'rate', 'update_at', 'status',
        )

    list_display_links = ('id',)
    ordering = ('pk',)


admin.site.register(Order, CustomOrderAdmin)
admin.site.register(Operation, CustomOperationAdmin)
