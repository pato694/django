from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Druh(models.Model):
    oznaceni_druhu = models.CharField(max_length=50, unique=True, verbose_name="Označení druhu auta",
                                      help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    KAROSERIE = (
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchback'),
        ('kombi', 'Kombi'),
        ('liftback', 'Liftback'),
        ('suv', 'SUV'),
        ('kabriolet', 'Kabriolet'),
        ('kupé', 'Kupé'),
    )
    oblast = models.CharField(max_length=20, choices=KAROSERIE, blank=True, default='sedan', verbose_name="Karoserie", help_text='Vyberte karoserii')

    class Meta:
        ordering = ["oznaceni_druhu"]
        verbose_name = 'Druh auta'
        verbose_name_plural = 'Druh auta'

    def __str__(self):
        return f"{self.oznaceni_druhu}, {self.oblast}"


class Auto(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název auta", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis auta")
    cena = models.IntegerField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadejte nezáporné desetinné číslo", verbose_name="Cena")
    STAV = (
        (5, 'nové'),
        (4, 'jako nové'),
        (3, 'málo ojeté'),
        (2, 'často jeté'),
        (1, 'hodně ojeté'),

    )
    stav = models.IntegerField(choices=STAV, blank=True, default=3, verbose_name="Stav auta", help_text='Vyberte označení stavu')
    ojete = models.IntegerField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadej pocet najetych kilometetru", verbose_name="kilometry")
    sila = models.IntegerField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadej pocet konskych sil", verbose_name="Počet koní")
    spotreba = models.FloatField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadej prumernou spotrebu", verbose_name="Průměrná spotřeba")
    foto = models.ImageField(upload_to='zbozi/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka auta")
    druh = models.ForeignKey(Druh, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["-cena", "nazev"]
        verbose_name = 'Auto'
        verbose_name_plural = 'Auto'

    def __str__(self):
        return f"{self.nazev}, {self.cena}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
