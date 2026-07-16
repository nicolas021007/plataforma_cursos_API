from tortoise import fields
from tortoise.models import Model

class AlunoModel(Model): 

    id = fields.CharField(pk = True, max_length = 36)
    nome =fields.CharField(max_length = 100)
    email = fields.CharField(max_length = 100, unique =True)
    senha_hash = fields.CharField(max_length = 255)
    data_nascimento = fields.DateField()
    ativo = fields.BooleanField(default = True)
    telefone = fields.CharField(max_length = 20, null = True)
    data_cadastro = fields.DatetimeField(auto_now_add = True)
    class Meta:
        table = "alunos"

    def __str__(self) ->str:
        return self.nome

