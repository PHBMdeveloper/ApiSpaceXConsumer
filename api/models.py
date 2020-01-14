from django.db import models

from django.db.models import CharField, Model
from django_mysql.models import ListCharField

# Create your models here.
class ProximoLancamento(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class UltimoLancamento(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class ProximosLancamento(models.Model):
    flight_number = models.CharField(max_length=150)
    mission_name = models.CharField(max_length=150)
    #mission_id = models.CharField(max_length=150) não conseguir importar
    launch_year = models.CharField(max_length=150)
    launch_date_unix = models.CharField(max_length=150)
    launch_date_utc = models.CharField(max_length=150)
    launch_date_local = models.CharField(max_length=150)
    is_tentative = models.CharField(max_length=150)
    tentative_max_precision = models.CharField(max_length=150)
    tbd = models.CharField(max_length=150)
    #launch_window = models.CharField(max_length=150)
    details = models.CharField(max_length=150)

    def __str__(self):
        return self.flight_number


class LancamentosPassado(models.Model):
    flight_number = models.CharField(max_length=150)
    mission_name = models.CharField(max_length=150)
    #mission_id = models.CharField(max_length=150) não conseguir importar
    launch_year = models.CharField(max_length=150)
    launch_date_unix = models.CharField(max_length=150)
    launch_date_utc = models.CharField(max_length=150)
    launch_date_local = models.CharField(max_length=150)
    is_tentative = models.CharField(max_length=150)
    tentative_max_precision = models.CharField(max_length=150)
    tbd = models.CharField(max_length=150)
    #launch_window = models.CharField(max_length=150)
    details = models.CharField(max_length=150)

    def __str__(self):
        return self.flight_number
