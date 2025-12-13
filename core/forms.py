from django import forms
from .models import Cliente

# Classi CSS per lo stile grigio
BOOTSTRAP_INPUT = "form-control shadow-none bg-light border-secondary-subtle"
BOOTSTRAP_SELECT = "form-select shadow-none bg-light border-secondary-subtle"


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cf", "rag_soc", "indirizzo", "citta"]
        widgets = {
            "cf": forms.TextInput(attrs={"class": BOOTSTRAP_INPUT}),
            "rag_soc": forms.TextInput(attrs={"class": BOOTSTRAP_INPUT}),
            "indirizzo": forms.TextInput(attrs={"class": BOOTSTRAP_INPUT}),
            "citta": forms.TextInput(attrs={"class": BOOTSTRAP_INPUT}),
        }


class ClienteSearchForm(forms.Form):
    cf = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": BOOTSTRAP_INPUT, "placeholder": "Codice Fiscale"}
        ),
    )
    rag_soc = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": BOOTSTRAP_INPUT, "placeholder": "Ragione Sociale"}
        ),
    )
    citta = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": BOOTSTRAP_INPUT, "placeholder": "Città"}
        ),
    )


class UtenzaSearchForm(forms.Form):
    cliente_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"class": BOOTSTRAP_INPUT, "placeholder": "ID Cliente"}
        ),
    )
    stato = forms.ChoiceField(
        choices=[("", "-- Tutti --"), ("attivo", "Attivo"), ("inattivo", "Inattivo")],
        required=False,
        widget=forms.Select(attrs={"class": BOOTSTRAP_SELECT}),
    )
    citta = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": BOOTSTRAP_INPUT, "placeholder": "Città"}
        ),
    )


class FatturaSearchForm(forms.Form):
    numero = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"class": BOOTSTRAP_INPUT, "placeholder": "N. Fattura"}
        ),
    )
    data_da = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": BOOTSTRAP_INPUT, "type": "date"}),
    )
    data_a = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": BOOTSTRAP_INPUT, "type": "date"}),
    )


class LetturaSearchForm(forms.Form):
    utenza_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"class": BOOTSTRAP_INPUT, "placeholder": "ID Utenza"}
        ),
    )
    fattura_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"class": BOOTSTRAP_INPUT, "placeholder": "N. Fattura"}
        ),
    )
    data_da = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": BOOTSTRAP_INPUT, "type": "date"}),
    )
    data_a = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": BOOTSTRAP_INPUT, "type": "date"}),
    )
