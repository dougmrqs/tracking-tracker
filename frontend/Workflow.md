## Curso de desenvolvimento do front-end.

Definido o firmware para renderização das páginas como Flask, será utilizado o Pipenv como gestor de pacotes.
Tendo certeza que está ativo um ambiente com Python e Pip, executa-se:

`pip install pipenv`

No diretório desejado, inicia-se o pipenv com:

`pipenv --three` (a tag --three indica a versão do python a ser instanciada)
`pipenv shell` 

O ambiente estando ativo, instala-se os pacotes com o comando:

`pipenv install nomedopacote`

O primeiro pacote instalado é o "flask".


### Formulário de Query

Para filtrar os dados, espera-se parâmetros de filtragem advindos de um formulário Flask-WTF.
Um serviço de segurança denominado CSRF é presente, então é necessária autenticação. **estudar**



#### Ref.:
Gerenciando seu projeto Python com Pipenv:
https://imasters.com.br/py/gerenciando-seu-projeto-python-com-o-pipenv

Markdown Cheatsheet:
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

Modelo de Dashboard Gratuito do Bootstrap:
https://startbootstrap.com/themes/sb-admin-2/

Como criar um aplicativo Flask e realizar Deploy na nuvem:
https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
