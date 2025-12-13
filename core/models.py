from django.db import models


class Cliente(models.Model):
    codice = models.AutoField(primary_key=True)
    cf = models.CharField(max_length=16, unique=True, verbose_name="Codice Fiscale")

    rag_soc = models.CharField(
        max_length=100, verbose_name="Ragione Sociale", db_column="ragSoc"
    )

    indirizzo = models.CharField(max_length=100)
    citta = models.CharField(max_length=60, verbose_name="Città")

    class Meta:
        db_table = "cliente"
        verbose_name_plural = "Clienti"
        ordering = ["rag_soc"]

    def __str__(self):
        return self.rag_soc


class Utenza(models.Model):
    codice = models.AutoField(primary_key=True)

    STATO_CHOICES = [("attivo", "Attivo"), ("inattivo", "Inattivo")]

    # db_column='cliente' gestisce la FK senza _id
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="utenze", db_column="cliente"
    )

    # Mappatura data apertura
    data_apertura = models.DateField(db_column="dataAp")

    indirizzo = models.CharField(max_length=100)
    citta = models.CharField(max_length=60, verbose_name="Città")
    stato = models.CharField(max_length=10, choices=STATO_CHOICES, default="attivo")

    # Mappatura data chiusura
    data_chiusura = models.DateField(null=True, blank=True, db_column="dataCh")

    class Meta:
        db_table = "utenza"
        verbose_name_plural = "Utenze"

    def __str__(self):
        return f"Utenza {self.codice} - {self.citta}"


class Fattura(models.Model):
    numero = models.AutoField(primary_key=True)
    data = models.DateField()
    imponibile = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    totale = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "fattura"
        verbose_name_plural = "Fatture"

    def __str__(self):
        return f"Fattura n.{self.numero}"


class Lettura(models.Model):
    numero = models.AutoField(primary_key=True)

    utenza = models.ForeignKey(
        Utenza, on_delete=models.CASCADE, related_name="letture", db_column="utenza"
    )

    fattura = models.ForeignKey(
        Fattura,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="fattura",
        related_name="letture",
    )

    data = models.DateField()
    valore = models.IntegerField()

    class Meta:
        db_table = "lettura"
        verbose_name_plural = "Letture"
