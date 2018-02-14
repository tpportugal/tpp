# TPP API
#### Aplicação para unificar os transportes públicos de Portugal

[![Build Status](https://travis-ci.org/glaand/tpp.svg?branch=master)](https://travis-ci.org/glaand/tpp)

***

#### Canais de comunicação 

**[Slack](https://join.slack.com/t/tpportugal/shared_invite/enQtMzEwOTI3ODg0MDk2LTZmNjYxOWVmZTBkN2EwNWUzMGFhOGQ2MWM0YmQ4NGUxMTU1ZjcwMDQxMDljMzU0Njg0ODcwOGIyODUxMjIzNmI)**

### Guião de contribuição para este projeto
https://github.com/glaand/tpp/blob/master/CONTRIBUTING.md

### Introdução
A intenção deste projecto é fornecer uma interface comum para o sistema de transporte públicos em Portugal.

O projecto consiste em 3 sub-projectos:
 - Modelo entidade relacionamento
 - Lógica de negócio
 - Saída de dados

### Dados iniciais / Migrações
Os dados iniciais disponíveis neste projecto depois das migrações são:
 - Todos os distritos de Portugal
 - Todas as cidades de Portugal


### Requisitos

```
docker >= 2
docker-compose >= 1.18
```

### Instalação
Sigam as instruções de comandos dadas abaixo:

- Façam um clone do repositório (SSH ou HTTPS)

```
# SSH
git clone --recurse-submodules git@github.com:glaand/tpp.git
# ou
#HTTPS
git clone --recurse-submodules https://github.com/glaand/tpp.git
```
- Entrem na pasta, façam a migração do projecto e iniciem a aplicação.

```
cd tpp/
docker-compose run --rm web python manage.py migrate
docker-compose up
```

Depois de o projecto estar construído e a correr, podem aceder à aplicação usando uns dos endereços dados no tópico *Saída de dados*:

### Saída de dados

#### Visão geral da API

http://0.0.0.0:8000

#### API em formato de JSON

http://0.0.0.0:8000/?format=json

#### API em formato de GraphQL

http://0.0.0.0:8000/graphql/
