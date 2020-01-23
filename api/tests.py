from django.test import TestCase
from .models import ProximosLancamento, LancamentosPassado
from rest_framework.response import Response
import urllib3
import json


class ProximosLancamentoTestCase(TestCase):
    def setUp(self):
        self.ProximosLancamento = ProximosLancamento.objects.create(
            flight_number="flight_number")
        self.ProximosLancamento = ProximosLancamento.objects.create(
            mission_name="mission_name")

    def test_Criacao(self):
        ''' Teste de criação no db '''
        assert ProximosLancamento.objects.all().count() == 2

    def test_Excluir(self):
        ''' Teste de exclusão no db '''
        ProximosLancamento.objects.all().delete()
        assert ProximosLancamento.objects.all().count() == 0

    def test_ProximoLancamento(self):
        ''' Teste de quantidade origem e destino '''
        http = urllib3.PoolManager()
        r = http.request('GET', 'https://api.spacexdata.com/v3/launches/next')
        j = json.loads(r.data.decode('utf-8'))
        print('ProximoLancamento =', len(j))
        assert len(j) == 30
        return Response(j)

    def test_UltimoLancamento(self):
        ''' Teste de quantidade origem e destino '''
        http = urllib3.PoolManager()
        r = http.request(
            'GET', 'https://api.spacexdata.com/v3/launches/latest')
        j = json.loads(r.data.decode('utf-8'))
        print('UltimoLancamento =', len(j))
        assert len(j) == 30
        return Response(j)

    def test_ProximosLancamentos(self):
        ''' Teste de quantidade origem e destino '''
        http = urllib3.PoolManager()
        r = http.request(
            'GET', 'https://api.spacexdata.com/v3/launches/upcoming')
        j = json.loads(r.data.decode('utf-8'))
        print('ProximosLancamentos =', len(j))
        assert len(j) == 15
        return Response(j)

    def test_LancamentosPassado(self):
        ''' Teste de quantidade origem e destino '''
        http = urllib3.PoolManager()
        r = http.request(
            'GET', 'https://api.spacexdata.com/v3/launches/past')
        j = json.loads(r.data.decode('utf-8'))
        print('LancamentosPassados =', len(j))
        assert len(j) == 88
        return Response(j)
