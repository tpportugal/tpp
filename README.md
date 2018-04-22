# TPP
#### Projeto para unificação informativa dos transportes públicos de Portugal

[![Guia de Contribuição](https://img.shields.io/badge/%E2%9D%A4-Guia%20de%20contribui%C3%A7%C3%A3o-blue.svg)](https://github.com/tpportugal/tpp/blob/master/CONTRIBUTING.md)
[![Canal de Comunicação](https://img.shields.io/badge/Canal%20de%20Comunica%C3%A7%C3%A3o-Slack-orange.svg)]((https://join.slack.com/t/tpportugal/shared_invite/enQtMzEwOTI3ODg0MDk2LTZmNjYxOWVmZTBkN2EwNWUzMGFhOGQ2MWM0YmQ4NGUxMTU1ZjcwMDQxMDljMzU0Njg0ODcwOGIyODUxMjIzNmI))
[![Administradores](https://img.shields.io/badge/Administradores-3-red.svg)](https://github.com/tpportugal/tpp/blob/master/ADMINS.md) 
  
**Read this in other languages**: [English](https://github.com/tpportugal/tpp/blob/master/README_EN.md)
***

## Finalidade

Este projeto pretende unificar todos os transportes públicos de Portugal numa única aplicação, isto é, a unificação de meios de transporte, horários e rotas num único sistema para que o utilizador, neste caso, o viajante consiga mover-se em Portugal com maior facilidade apenas introduzindo o local de partida e o local de chegada.

## Funcionamento

Para que a aplicação possa mostrar a melhor rota entre o ponto A e o ponto B é necessário ter em nossa posse vários tipos de dados como: Regiões, Rotas, Meios de transporte, Operadoras de transporte e Horários. A partir destes dados o nosso algoritmo conseguirá calcular a rota mais eficiente para o utilizador, isto é, que tenha o menor número de mudanças de linha, como também a duração da viagem. Obviamente é necessário também que os dados estejam atualizados conforme comunicado pelas operadoras.

## Obtenção de dados

Geralmente por canais digitais onde as operadoras têm os seus dados publicados. Haverá casos em que as operadoras não têm horários em formato digital, aí teremos que fazer uma digitalização dos horários e aplicar um algoritmo de reconhecimento de padrões que extraia os dados por nós, isto para evitar erros humanos na introdução de dados

# Serviços

**Valhalla** [Motor de rotas] - https://github.com/tpportugal/tpp_valhalla  
**Banco de dados** [API do serviço web centralizado TPP] - https://github.com/tpportugal/tpp_banco_de_dados  
**Explorador** [Explorador de redes de transportes em Portugal] - https://github.com/tpportugal/tpp_explorador  
**APP** [Frontend para o serviço TPP] - https://github.com/tpportugal/tpp_app  
**Expedidor** [Administrador do Backend do Banco de Dados] - https://github.com/tpportugal/tpp_expedidor  
**Registo de feeds** [Diretoria de feeds de operadoras] - https://github.com/tpportugal/tpp_registo_de_feeds  
**Admin** [Projeto Django TPP Admin management] - https://github.com/tpportugal/tpp_admin  
