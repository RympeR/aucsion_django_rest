from django.contrib import admin
from .models import *
from django.contrib.admin import DateFieldListFilter


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'username', 'first_name', 'last_name',
    ]
    list_display_links = [
        'pk'
    ]
    search_fields = [
        'first_name', 'username',
    ]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'seller', 'aucsion', 'product_type'
    ]
    search_fields = [
        'seller__username', 'seller__first_name'
    ]


@admin.register(AucsionHistory)
class AucsionHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'buyer', 'aucsion', 'bet',
    ]
    search_fields = [
        'buyer__username', 'buyer__first_name'
    ]


@admin.register(Aucsion)
class AucsionAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'min_bet', 'max_bet', 'stock_price',
    ]
    list_filter = (
        ('start_datetime', DateFieldListFilter),
        ('end_datetime', DateFieldListFilter),
    )
    ordering = '-start_datetime',


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'purchase', 'address'
    ]
    

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'expert', 'product'
    ]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'datetime', 'buyer', 'final_price',
    ]
    list_filter = (
        ('datetime', DateFieldListFilter),
    )
    search_fields = [
        'buyer__username', 'buyer__first_name'
    ]
    ordering = '-datetime',


@admin.register(BuyerBlackList)
class BuyerBlackListAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'buyer'
    ]
    search_fields = [
        'buyer__username', 'buyer__first_name'
    ]
    list_display_links = 'pk',


admin.site.register(Buyer)
admin.site.register(Expert)


@admin.register(SellerBlackList)
class SellerBlackListAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'seller'
    ]
    search_fields = [
        'user__username', 'user__first_name',
        'seller__username', 'seller__first_name',
    ]
    list_display_links = [
        'user'
    ]


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'expertise'
    ]
    list_display_links = 'user',
    search_fields = [
        'user__username', 'user__first_name'
    ]
