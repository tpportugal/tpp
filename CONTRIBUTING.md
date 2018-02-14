# Contribuir para o TTP

:+1: :tada: Primeiramente, um grande obrigado pela tua contribuição com o teu tempo! :tada: :+1:

Se ainda não te juntaste ao nosso canal de comunicação Slack, poderás fazê-lo [aqui!](https://join.slack.com/t/tpportugal/shared_invite/enQtMzEwOTI3ODg0MDk2LTZmNjYxOWVmZTBkN2EwNWUzMGFhOGQ2MWM0YmQ4NGUxMTU1ZjcwMDQxMDljMzU0Njg0ODcwOGIyODUxMjIzNmI)

Queremos que desenvolvas características do projeto que te entusiasmem!!!

Se ficares preso em qualquer ponto, estás à vontade para criar um Issue no GitHub.

Todos os membros da nossa comunidade são obrigados a seguir o nosso [código de conduta](https://github.com/glaand/tpp/blob/master/CODE_OF_CONDUCT.md). Certifica-te que és acolhedor e amigável em todos os nossos espaços.

Abaixo estão algums recursos importantes para quem começa:

 - [Conceito do TPP](https://github.com/glaand/tpp/wiki/TPP---Conceito)
 - [O nosso Roadmap](https://github.com/glaand/tpp/wiki/Roadmap)

## Contribuir no desenvolvimento

Se quiseres mergulhar profundamente e ajudar com o desenvolvimento do TPP, instala primeiro o projeto localmente de acordo com o nosso [Guia de Instalação](https://github.com/glaand/tpp/blob/master/README.md). Depois disso, sugerimos que vejas os Issues no nosso [Issue Tracker](https://github.com/glaand/tpp/issues) que estejam marcados como `Good First Issue`. Estes Issues são ótimos para teres um começo suave e não te colocam em frente ás partes mais complexas do sistema.

Se quiseres trabalhar em tarefas mais desafiadoras, então segue os seguintes marcadores: `data`, `feature`, `bug`. Estes Issues têm uma visão geral e descrição do pretendido. Este tipo de Issues serão os ideais para começares. Dito isto, estes não são necessariamente os Issues mais fáceis.

### Testing

Para que possamos garantir a funcionalidade da aplicação, é importante correr vários testes no software para anular a possibilidade de erros lógicos.

* Para correr os testes através de django executa o commando correspondente ao teu Environment:
    * Para Production-Environment:
        `docker-compose run -rm web python manage.py test`
    * Para Development-Environment:
        `docker-compose -f docker-compose.development.yml run -rm web python manage.py test`

* Certifica-te que a característica soluciona realmente o problema em questão.

### Estilo de código (Coding style)

Aqui seguimos o estilo de código recomendado pela Django que é `pep8`.

Temos um ficheiro na raíz do projeto chamado `qa_check.sh`. Executa esse ficheiro e faz as alterações visuais sugeridas pelo [`flake8`](http://flake8.pycqa.org/en/latest/). Caso verifiques que não tem sentido nenhum fazer a alteração sugerida pelo flake8, exclui o ficheiro da verificação. Podes fazer isso introduzindo o **selector** do nome do ficheiro no ficheiro: `setup.cfg`. Faz essa alteração no seguinte branch: `coding-style`. Se o branch ainda não existir, podes criá-lo.

### Introdução dos teus dados no AUTHORS.md

Se for o teu primeiro commit, adiciona o teu nome e contacto no ficheiro [AUTHORS.md](https://github.com/glaand/tpp/blob/master/AUTHORS.md)

---

## Contribuir na recolha de dados

Com centenas de operadoras de transportes públicos, também vamos precisar da tua ajuda na recolha de dados. Certifica-te que os dados recolhidos estejam disponíveis ao público.

Para contribuir com carregamento de horários em formato (PDF ou JPG) poderás aceder este link e preencher o formulário: https://www.tpp.pt/upload

### Obtenção dos dados das operadoras em formato GTFS

É necessário haver uma especificação de dados para que a integração e a manuntenção dos dados sejam eficientes. Poderão ler o documento publicado pela Google neste [link](https://developers.google.com/transit/gtfs/reference)

Nem todas as empresas, infelizmente, aderem ao idealismo do **Open-Data**, isso implica que haja burocracias na obtenção de dados. Caso queiram contactar as operadoras de transporte, falem primeiro com um dos membros da administração do projeto: [glaand (André Glatzl)](mailto:andre@glatzl.me) , [Rui-Santos (Rui J Santos)](mailto:rui.s@gmx.us)
