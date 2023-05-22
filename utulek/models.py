import os

from django.db import models


# Create your models here.


class mesto(models.Model):
    nazev_mesta = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='název města',
        help_text='Zadej název města'
    )

    kraj = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='název kraje',
        help_text='Zadej název kraje'
    )

    psc = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        verbose_name='PSČ'
    )

    class Meta:
        verbose_name = 'Město',
        verbose_name_plural = 'Města'

        def __str__(self):
            return self.nazev_mesta


class utulek(models.Model):
    name = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='název útulku',
        help_text='Zadej název útulku'
    )

    adresa = models.CharField(
        max_length=45,
        unique=True,
        verbose_name='adresa útulku',
        help_text='Zadej adresu útulku'
    )

    mesto_nazev = models.ForeignKey(
        'mesto',
        on_delete=models.CASCADE,
        verbose_name='Město',
    )

    class Meta:
        verbose_name = 'Útulek',
        verbose_name_plural = 'Útulky'

    def __str__(self):
        return self.name


class pes(models.Model):
    jmeno_psa = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='jméno psa',
        help_text='Zadej jméno psa'
    )

    rasa = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='rasa psa',
        help_text='Zadej rasu psa'
    )

    popis = models.TextField(
        null=True,
        blank=True,
        verbose_name='popis'
    )

    utulek_nazev = models.ForeignKey(
        'utulek',
        on_delete=models.CASCADE,
        verbose_name='Útulek',
    )

    class Meta:
        verbose_name = 'Pes',
        verbose_name_plural = 'Psi'

    def __str__(self):
        return f'{self.jmeno_psa} ({self.utulek_nazev})'


class zajemce(models.Model):
    jmeno_zajemce = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='jméno zájemce',
        help_text='Zadej jméno zájemce'
    )

    prijmeni_zajemce = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='Příjmení Ošetřovatele',
        help_text='Zadej Příjmení Ošetřovatele'
    )

    mobil_zajemce = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='mobil'
    )

    email = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='email zájemce',
        help_text='Zadej email zájemce'
    )

    mesto_nazev = models.ForeignKey(
        'mesto',
        on_delete=models.CASCADE,
        verbose_name='Město',
    )

    class Meta:
        verbose_name = 'Zájemce',
        verbose_name_plural = 'Zájemci'

    def __str__(self):
        return f'{self.jmeno_zajemce} ({self.mesto_nazev})'


class osetrovatel(models.Model):
    jmeno = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='Jméno Ošetřovatele',
        help_text='Zadej Jméno Ošetřovatele'
    )

    prijmeni = models.CharField(
        max_length=45,
        unique=False,
        verbose_name='Příjmení Ošetřovatele',
        help_text='Zadej Příjmení Ošetřovatele'
    )

    mobil = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='mobil'
    )

    utulek_nazev = models.ForeignKey(
        'utulek',
        on_delete=models.CASCADE,
        verbose_name='Útulek název',
    )

    class Meta:
        verbose_name = 'Ošetřovatel',
        verbose_name_plural = 'Ošetřovatelé'

    def __str__(self):
        return f'{self.jmeno} ({self.utulek_nazev})'
