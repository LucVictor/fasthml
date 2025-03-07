from peewee import *
import os
from datetime import date

psql_db = PostgresqlDatabase(
    'postgres',  # Required by Peewee.
    user='postgres',  # Will be passed directly to psycopg2.
    password='CnEFJCNi8HWF6tFMOfujqPoa5BV3ObhoQAMizr3AmOmvU8InFoRQeoKVPtnhUpMw',  # Ditto.
    host='191.252.177.179',
    port=3351)  # Ditto.


class Produto(Model):
    codigo = IntegerField()
    nome = CharField()

    class Meta:
        database = psql_db 

class Pessoas(Model):
    nome = CharField()
    cargo = CharField()

    class Meta:
        database = psql_db

class Obs(Model):
    codigo = AutoField()
    data = DateField()
    cliente = CharField()
    codigoCliente = IntegerField()
    status = BooleanField()
    picote = CharField()
    solicitante = CharField()
    motorista = CharField()
    numeroPedido = IntegerField()
    usuario = CharField()
    ultimaAtualizacao = DateField()

    class Meta:
        database = psql_db

class Itens(Model):
    codigo = AutoField()
    codigoObs = IntegerField()
    nome = CharField()
    quantidade = IntegerField()
    status = CharField()
    motivo = CharField()

    class Meta:
        database = psql_db


class Clientes(Model):
    codigo = IntegerField()
    fantasia = CharField()
    nome = CharField()
    cnpj =  CharField()
    rua = CharField()
    numero = CharField()
    bairro = CharField()
    cidade = CharField()

    
    class Meta:
        database = psql_db

class Usuarios(Model):
    usuario = CharField(unique=True)
    senha = CharField()
    
    class Meta:
        database = psql_db

psql_db.connect()


