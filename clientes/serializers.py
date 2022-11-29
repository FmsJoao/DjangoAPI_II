from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, nome_valido, rg_valido, celular_valido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "The cpf needs to be valid"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "The name can only have letters"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "The RG must have 9 digits"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O celular deve seguir o padrão: 00 00000-0000"})
        return data

