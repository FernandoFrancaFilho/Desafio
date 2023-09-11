from django.db import models

class Cnh(models.Model):
    nome_completo = models.CharField(max_length=200)
    registro_geral = models.IntegerField()
    cpf = models.CharField(max_length=14, unique=True)
    data_de_nascimento = models.CharField(max_length=10, unique=True)
    número_de_registro = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f'CNH: {self.nome_completo}'

class Carro(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50, default='cor padrão')
    ano = models.IntegerField()
    imagem_do_veiculo = models.ImageField(upload_to='carros/', blank=True, null=True)
    
    cnh = models.ForeignKey(Cnh, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Carro: {self.marca} {self.modelo}'