from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)

from .models import Member, Address, BankDetails

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('vorname', 'nachname', 'emailadresse', 'telefonnummer')
    search_fields = ('vorname', 'nachname', 'emailadresse')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('strasse', 'hausnummer', 'stadt', 'postleitzahl')
    search_fields = ('strasse', 'stadt')

@admin.register(BankDetails)
class BankDetailsAdmin(admin.ModelAdmin):
    list_display = ('kontoinhaber', 'iban', 'bic')
    search_fields = ('kontoinhaber', 'iban')
