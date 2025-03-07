from peewee import *
import os
from datetime import date

psql_db = PostgresqlDatabase(
    os.environ.get("DB_NAME", "postgres"),      # Nome do banco (padrão: postgres)
    user=os.environ.get("DB_USER", "postgres"),  # Usuário do banco
    password=os.environ.get("DB_PASSWORD", ""),  # Senha do banco
    host=os.environ.get("DB_HOST", "localhost"),  # IP do banco
    port=int(os.environ.get("DB_PORT", 5432))  # Porta do banco (padrão: 5432)
)

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


