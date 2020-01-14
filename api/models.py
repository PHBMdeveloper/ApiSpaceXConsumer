from django.db import models

from django.db.models import CharField, Model, TextField
from django_mysql.models import ListCharField

# Create your models here.
class ProximoLancamento(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome


class UltimoLancamento(models.Model):
    nome = models.TextField

    def __str__(self):
        return self.nome


class ProximosLancamento(models.Model):
    flight_number = models.TextField()
    mission_name = models.TextField()
    #mission_id = models.TextField() não conseguir importar
    launch_year = models.TextField()
    launch_date_unix = models.TextField()
    launch_date_utc = models.TextField()
    launch_date_local = models.TextField()
    is_tentative = models.TextField()
    tentative_max_precision = models.TextField()
    tbd = models.TextField()
    #launch_window = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.flight_number


class LancamentosPassado(models.Model):
    flight_number = models.TextField()
    mission_name = models.TextField()
    #mission_id = models.TextField() não conseguir importar
    launch_year = models.TextField()
    launch_date_unix = models.TextField()
    launch_date_utc = models.TextField()
    launch_date_local = models.TextField()
    is_tentative = models.TextField()
    tentative_max_precision = models.TextField()
    tbd = models.TextField()
    #launch_window = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.flight_number
