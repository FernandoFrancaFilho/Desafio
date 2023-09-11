# desafio_workshop_backend_2023.2

- Observação extremamente importante: para iniciar o todo o procedimento para ver se o desafio está correto, será preciso realizar esses 4 códigos em sequência:
```ps1

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver  
```
Nesse desafio foi preciso realizar a criação de uma API pelo Django Rest Framework. Por meio desse READ.ME, irei explicar as etapas que foram feitas para conseguir Resolver esse desafio, com os seguintes Requisitos:

- Funcionamento das 4 operações(get, post, put e delete)
- Conexão com a sgbd a escolha
- Mínimo de 2 entidades referentes ao tema.
- Criar requeriments.txt
- Relacionamento entre entidades
- Paginação
- Usar funções do DjangoRestFramework que não foram vistas no Workshop.
- Organização na identação
- Nome de pastas e arquivos intuitivos a demanda:
- Fazer o push do projeto na Branch separada no Github.com com uma readme explicando todo o funcionamento da operação de CRUD

## Primeiros passos:

Primeiramente iremos utilizar o Visual Studio Code para realizar a edição de códigos, mas pode ser utilizado qualquer outro editor da escolha de quem irá realizar o procedimento.

Logo após será preciso criar uma pasta vázia que será utilizada para instalar os arquivos, no meu caso foi criado a pasta CarDastro(pois a API será para recolhimento de informações de carros e dos usuários que irão utilizar os mesmos).

Após selecionar a pasta, iremos abrir um terminal no proprio editor e colocar os seguintes códigos:

- Criação de um ambiente virtual em Python

```ps1
python -m venv venv
```

- Ativação do ambiente virtual:

```ps1
.\venv\Scripts\activate.ps1
```

- Instalação do Django Rest Framework

 ```ps1
pip install djangorestframework
```
- Instalação do Banco de Dados PostGree Admin

 ```ps1
python -m pip install Pillow

pip install psycopg2

pip install psycopg2-binary

pip install postgres

pip install sqlparse
```
- Criação da pasta do projeto

```ps1
django-admin startproject nomedapasta . <no meu caso, CarDastro>
```

- Criação da pasta do app

```ps1
python .\manage.py startapp nomedoapp <No meu caso, car> 
```

## Modificação e Codificação:

- Após a criação da pasta projeto, será preciso ir em ```settings.py``` , e realizar a 2 inclusões. A primeira delas sendo na parte de ```INSTALLED_APPS```.

```ps1
    'rest_framework',
    'car',
```

- E a segunda modificação será para a integração com o SGBD, que será feita na parte de ```DATABASES```, que também está em ```settings.py```.

```ps1
{
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'desafio',
             'USER': 'postgres',
             'PASSWORD': '123456789',
             'HOST': 'localhost',
             'PORT': '5432',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'ATOMIC_REQUESTS':True
}
```
- A terceira e última modificação que será feita no ```settings.py```, será para adicionar a paginação. e para isso terá que ser adicionando essa linha de código, logo abaixo da parte de ```DATABASES```.

```ps1
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 1
}
```

- Obs: A parte do SGBD pode variar, por conta que cada um pode modificar seu SGBD da forma que achar melhor, mudando senha, nome e porta.

- Logo após modificar essas configurações, será preciso realizar a inclusão dos arquivos ```urls.py``` e ```serializers.py``` em nosso app.

- Agora segue a códificação do arquivo ```models.py``` :

```ps1
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
```

- Após essa, temos a parte de ```serializers.py```:

```ps1
from rest_framework import serializers
from car.models import Carro, Cnh

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'

class CnhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnh
        fields = '__all__'
```

- Em seguida será feita a modificação na parte de ```views.py```:

```ps1
from django.shortcuts import render
from rest_framework import viewsets
from .models import Carro, Cnh
from .serializers import CarroSerializer, CnhSerializer

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

class CnhViewSet(viewsets.ModelViewSet):
    queryset = Cnh.objects.all()
    serializer_class = CnhSerializer
```

- Próximo passo será configurar a ```urls.py```:

```ps1
from rest_framework import routers
from .views import CarroViewSet, CnhViewSet

router = routers.DefaultRouter()
router.register(r'cnhs', CnhViewSet)
router.register(r'carros', CarroViewSet) 
     
urlpatterns = router.urls
```

- E agora o último passo da códificação será no ```urls.py``` do projeto:

```ps1
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car.urls'))
]
```

- Após realizer todos os procedimentos mostrados anteriormente, pode ser feito os comandos para verificar se a API foi feita com sucesso.

```ps1
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

- O terminal irá mostrar um Link, basta apenas clicar no mesmo e acessar, caso não consiga acessar dessa formam, basta digitar essá URL:

```
http://127.0.0.1:8000/
```

- E assim temos nossa API finalizada. 

## Observações finais:

- Será preciso baixar o PostgreeSQL para poder realizar a integração do SGBD, foi baixada a versão 14.9 no link abaixo:

```
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows
```

> Todos os conhecimentos colocados nessa documentação foram absorvidos através do Workshop realizado na Fábrica de Software 2023.2 Lab 8 Sala 2.

> O nome do projeto vem do trocadilho Car em inglês que significa carro e cadastro, fazendo a junção do mesmo e se tornando ```CarDastro```.