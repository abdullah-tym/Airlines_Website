from multiprocessing.connection import Client
from django.contrib import admin
from .models import Avion, Contact,Reserve, Utilisateur, Voyage
# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Contact)
admin.site.register(Voyage)
admin.site.register(Avion)
admin.site.register(Reserve)


######################################################################################################################

from .models import Flight, Seat


class SeatInline(admin.StackedInline):
    model = Seat
    extra = 1


class FlightAdmin(admin.ModelAdmin):
    inlines = [SeatInline]


admin.site.register(Flight, FlightAdmin)
admin.site.register(Seat)
