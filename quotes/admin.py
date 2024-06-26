from django.contrib import admin
from .models import Quotes

class QuotesAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')

admin.site.register(Quotes, QuotesAdmin)