from rest_framework.serializers import ModelSerializer
from api.models import (
    ProximoLancamento,
    UltimoLancamento,
    ProximosLancamento
)


class ProximoLancamentoSerializer(ModelSerializer):
    class Meta:
        model = ProximoLancamento
        fields = []


class UltimoLancamentoSerializer(ModelSerializer):
    class Meta:
        model = UltimoLancamento
        fields = []


class ProximosLancamentosSerializer(ModelSerializer):
    class Meta:
        model = ProximosLancamento
        fields = '__all__'


class LancamentosPassadoSerializer(ModelSerializer):
    class Meta:
        model = ProximosLancamento
        fields = '__all__'
