from django.contrib import admin
from .models import Transactions
# Register your models here.
admin.site.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'amount', 'timestamp', 'comment')
    search_fields = ('sender__owner__username', 'recipient__owner__username')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)