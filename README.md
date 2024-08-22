# Projeto Crimson

#### App para gestão de cadastro, atividades e acessos no contexto do departamento infantil de uma Igreja.

## Objetivo do Projeto

#### Atender as necessidades de uso de um departamento infantil de uma Igreja, com:

- registro de responsáveis
- registro de crianças
- aceite de termos de responsabilidade
- registro de necessidades especiais
- cadastro de eventos semanais e esporádicos
- registro de participates dos eventos
- geraçao de ferramentas para controle de acesso e responsabilidade nos eventos


### Passos do projeto:

. Definir Responsabilidades Juridicas a serem atendidas
. Recursos que a ferramenta devem atender
. Interface com as funcionalidades da ferramenta
. UML da estrutura dos dados que serão coletados e armazenados
.

#### Responsabilidades Juridicas

- definir informacoes para o termo de compromisso
- demandas do registro da crianca
- definir limitacoes de operacao (o que pode e nao pode)

#### Recursos e ferramentas

##### Hardware

-
-
-

##### Software

- codigo backend Python
    - pip: django, djangorestframework
    - django-admin startproject crimson
    - django-admin startapp api
    - python ./manage.py makemigrations
    - npm run dev
- Estrutura de dados Postgres
- queries em FastAPI
- Integraçao reconhecimento facil no Checkin