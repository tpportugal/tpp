# TPP API
#### Aplicação para unificar os transportes públicos de Portugal

[![Guião de contribuição](https://img.shields.io/badge/%E2%9D%A4-Gui%C3%A3o%20de%20contribui%C3%A7%C3%A3o-blue.svg)](https://github.com/glaand/tpp/blob/master/CONTRIBUTING.md)
[![Build Status](https://travis-ci.org/glaand/tpp.svg?branch=master)](https://travis-ci.org/glaand/tpp)
[![Canal de comunicação](https://img.shields.io/badge/Canal%20de%20comunica%C3%A7%C3%A3o-Slack-orange.svg)]((https://join.slack.com/t/tpportugal/shared_invite/enQtMzEwOTI3ODg0MDk2LTZmNjYxOWVmZTBkN2EwNWUzMGFhOGQ2MWM0YmQ4NGUxMTU1ZjcwMDQxMDljMzU0Njg0ODcwOGIyODUxMjIzNmI))


***

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
- Entrem na pasta e executem o script `set_deployment.sh`, da seguinte forma:

```bash
cd tpp/
bash set_development.sh
```

O script faz a migração do projecto.

Para iniciar a aplicação, sem voltar a instalar todas as dependências, escrevam no terminal, dentro da raiz do projecto:

```bash
bash start_development.sh
```

Depois de o projecto estar construído e a correr, podem aceder à aplicação usando uns dos endereços dados no tópico *Saída de dados*:

### Saída de dados

#### Visão geral da API

http://0.0.0.0:8000

#### API em formato de JSON

http://0.0.0.0:8000/?format=json

#### API em formato de GraphQL

http://0.0.0.0:8000/graphql/
