from peewee import *
from datetime import date

db = SqliteDatabase('banco.db')


class Produto(Model):
    codigo = IntegerField()
    nome = CharField()

    class Meta:
        database = db 

class Pessoas(Model):
    nome = CharField()
    cargo = CharField()

    class Meta:
        database = db 

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
        database = db

class Itens(Model):
    codigo = AutoField()
    codigoObs = IntegerField()
    nome = CharField()
    quantidade = IntegerField()
    status = CharField()
    motivo = CharField()

    class Meta:
        database = db


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
        database = db

db.connect()


