from django.contrib import admin
from .models import BankAccount



admin.site.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('owner', 'balance', 'card_number', 'expiration_date', 'cvv', 'created_at')
    search_fields = ('owner__username', 'card_number')
    list_filter = ('created_at', 'expiration_date')
    ordering = ('-created_at',)
    