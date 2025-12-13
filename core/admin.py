from django.contrib import admin
from .models import Cliente, Utenza, Fattura, Lettura


class UtenzaInline(admin.TabularInline):
    model = Utenza
    extra = 0
    readonly_fields = ("data_apertura",)
    classes = ["collapse"]


class LetturaInline(admin.TabularInline):
    model = Lettura
    extra = 0
    ordering = ("-data",)


# --- ADMIN MODELS ---


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("codice", "rag_soc", "cf", "citta", "count_utenze")
    list_display_links = ("rag_soc",)
    search_fields = ("rag_soc", "cf", "citta")
    list_filter = ("citta",)
    inlines = [UtenzaInline]
    ordering = ("rag_soc",)

    def count_utenze(self, obj):
        return obj.utenze.count()

    count_utenze.short_description = "# Utenze"


@admin.register(Utenza)
class UtenzaAdmin(admin.ModelAdmin):
    list_display = (
        "codice",
        "cliente_link",
        "citta",
        "indirizzo",
        "stato",
        "data_apertura",
    )
    list_filter = ("stato", "citta", "data_apertura")
    search_fields = ("cliente__rag_soc", "indirizzo", "citta")
    autocomplete_fields = ["cliente"]
    inlines = [LetturaInline]

    def cliente_link(self, obj):
        return obj.cliente

    cliente_link.short_description = "Cliente"
    cliente_link.admin_order_field = "cliente__rag_soc"


@admin.register(Fattura)
class FatturaAdmin(admin.ModelAdmin):
    list_display = ("numero", "data", "totale", "imponibile", "iva")
    list_filter = ("data",)
    ordering = ("-data",)
    date_hierarchy = "data"


@admin.register(Lettura)
class LetturaAdmin(admin.ModelAdmin):
    list_display = ("numero", "data", "valore", "utenza_link", "fattura")
    list_filter = ("data", "utenza__citta")
    search_fields = ("utenza__cliente__rag_soc",)
    ordering = ("-data",)

    def utenza_link(self, obj):
        return f"{obj.utenza.cliente} ({obj.utenza.citta})"

    utenza_link.short_description = "Utenza"
