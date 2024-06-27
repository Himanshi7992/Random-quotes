from django.contrib import admin
from .models import Quote, DailyQuote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')

class DailyQuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'day_of_year')

admin.site.register(Quote, QuoteAdmin)
admin.site.register(DailyQuote, DailyQuoteAdmin)
