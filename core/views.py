from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from .models import Cliente, Utenza, Fattura, Lettura
from .forms import (
    ClienteForm,
    ClienteSearchForm,
    UtenzaSearchForm,
    FatturaSearchForm,
    LetturaSearchForm,
)


def home(request):
    return render(request, "home.html", {"active_nav": "home"})


def cliente_list(request):
    form = ClienteSearchForm(request.GET)
    clienti = Cliente.objects.annotate(num_utenze=Count("utenze"))

    if form.is_valid():
        if form.cleaned_data["cf"]:
            clienti = clienti.filter(cf__icontains=form.cleaned_data["cf"])
        if form.cleaned_data["rag_soc"]:
            clienti = clienti.filter(rag_soc__icontains=form.cleaned_data["rag_soc"])
        if form.cleaned_data["citta"]:
            clienti = clienti.filter(citta__icontains=form.cleaned_data["citta"])

    return render(
        request,
        "cliente_list.html",
        {"clienti": clienti, "form": form, "active_nav": "clienti"},
    )


def cliente_create(request):
    title = "Nuovo Cliente"
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente creato correttamente.")
            return redirect("cliente_list")
    else:
        form = ClienteForm()
    return render(request, "cliente_form.html", {"form": form, "title": title})


def cliente_edit(request, pk):
    # pk mappa automaticamente a 'codice' grazie al model
    cliente = get_object_or_404(Cliente, pk=pk)
    title = f"Modifica {cliente.rag_soc}"
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente aggiornato.")
            return redirect("cliente_list")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "cliente_form.html", {"form": form, "title": title})


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    utenze_count = cliente.utenze.count()

    if request.method == "POST":
        if utenze_count > 0:
            messages.error(request, "Impossibile eliminare: esistono utenze associate.")
        else:
            cliente.delete()
            messages.success(request, "Cliente eliminato.")
        return redirect("cliente_list")

    return render(
        request,
        "cliente_confirm_delete.html",
        {"cliente": cliente, "utenze_count": utenze_count},
    )


def utenza_list(request):
    form = UtenzaSearchForm(request.GET)
    utenze = Utenza.objects.select_related("cliente").annotate(
        num_letture=Count("letture")
    )

    if form.is_valid():
        if form.cleaned_data["cliente_id"]:
            utenze = utenze.filter(cliente__codice=form.cleaned_data["cliente_id"])
        if form.cleaned_data["stato"]:
            utenze = utenze.filter(stato=form.cleaned_data["stato"])
        if form.cleaned_data["citta"]:
            utenze = utenze.filter(citta__icontains=form.cleaned_data["citta"])

    return render(
        request,
        "utenza_list.html",
        {"utenze": utenze, "form": form, "active_nav": "utenze"},
    )


def fattura_list(request):
    form = FatturaSearchForm(request.GET)
    fatture = Fattura.objects.annotate(num_letture=Count("letture")).order_by("-data")

    if form.is_valid():
        if form.cleaned_data["numero"]:
            fatture = fatture.filter(numero=form.cleaned_data["numero"])
        if form.cleaned_data["data_da"]:
            fatture = fatture.filter(data__gte=form.cleaned_data["data_da"])
        if form.cleaned_data["data_a"]:
            fatture = fatture.filter(data__lte=form.cleaned_data["data_a"])

    return render(
        request,
        "fattura_list.html",
        {"fatture": fatture, "form": form, "active_nav": "fatture"},
    )


def lettura_list(request):
    form = LetturaSearchForm(request.GET)
    letture = Lettura.objects.select_related("utenza__cliente", "fattura").order_by(
        "-data"
    )

    if form.is_valid():
        if form.cleaned_data["utenza_id"]:
            letture = letture.filter(utenza__codice=form.cleaned_data["utenza_id"])
        if form.cleaned_data["fattura_id"]:
            letture = letture.filter(fattura__numero=form.cleaned_data["fattura_id"])
        if form.cleaned_data["data_da"]:
            letture = letture.filter(data__gte=form.cleaned_data["data_da"])
        if form.cleaned_data["data_a"]:
            letture = letture.filter(data__lte=form.cleaned_data["data_a"])

    return render(
        request,
        "lettura_list.html",
        {"letture": letture, "form": form, "active_nav": "letture"},
    )
