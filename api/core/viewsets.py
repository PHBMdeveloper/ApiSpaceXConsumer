from rest_framework import viewsets
from rest_framework.response import Response

from api.models import (
    ProximoLancamento, 
    UltimoLancamento, 
    ProximosLancamento,
    LancamentosPassado )

from .serializers import (
    ProximoLancamentoSerializer,
    UltimoLancamentoSerializer,
    ProximosLancamentosSerializer, 
    LancamentosPassadoSerializer
    )

import urllib3
import json


class ProximoLancamentoViewSet(viewsets.ModelViewSet):
    queryset = ProximoLancamento.objects.all()
    serializer_class = ProximoLancamentoSerializer

    def list(self, request, *args, **kwargs):
        http = urllib3.PoolManager()
        r = http.request('GET', 'https://api.spacexdata.com/v3/launches/next')
        j = json.loads(r.data.decode('utf-8'))

        return Response(j)
        # return Response({
        #     "numero voo": j["flight_number"],
        #     "nome missao": j["mission_name"]
        # })  # inserir um lista


class UltimoLancamentoViewSet(viewsets.ModelViewSet):
    queryset = UltimoLancamento.objects.all()
    serializer_class = UltimoLancamentoSerializer

    def list(self, request, *args, **kwargs):
        http = urllib3.PoolManager()
        r = http.request(
            'GET', 'https://api.spacexdata.com/v3/launches/latest')
        j = json.loads(r.data.decode('utf-8'))

        return Response(j)


class ProximosLancamentoViewSet(viewsets.ModelViewSet):
    queryset = ProximosLancamento.objects.all()
    serializer_class = ProximosLancamentosSerializer

    # def list(self, request, *args, **kwargs):
    #     http = urllib3.PoolManager()
    #     r = http.request(
    #         'GET', 'https://api.spacexdata.com/v3/launches/upcoming')
    #     j = json.loads(r.data.decode('utf-8'))

    #     return Response(j)

class LancamentosPassadoViewSet(viewsets.ModelViewSet):
    queryset = LancamentosPassado.objects.all()
    serializer_class = LancamentosPassadoSerializer