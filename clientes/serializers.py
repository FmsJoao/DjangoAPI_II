from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, nome_valido, rg_valido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "The cpf must have 11 digits"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "The name can only have letters"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "The RG must have 9 digits"})
        return data

    # def validate_celular(self, celular):
    # if len(celular) <11:
    # raise serializers.ValidationError("The celular must have at least 11 digits")
    # return celular
