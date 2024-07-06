# Nota10 - Gerenciamento de Tarefas para Estudantes

Este projeto é parte de um aplicativo de gerenciamento de tarefas desenvolvido para a disciplina Desenvolvimento Full Stack Básico.


## Estrutura do Projeto
A estrutura do projeto está organizada da seguinte forma:

MeuMVP/  
├── backend/  
│   ├── env/  
│   ├── static/  
│   │   ├── swagger.json  
│   ├── __init__.py  
│   ├── app.py  
│   ├── models.py  
│   ├── routes.py  
├── frontend/  
│   ├── css/  
│   │   ├── style.css  
│   ├── js/  
│   │   ├── script.js  
│   ├── index.html  
├── instance/  
│   ├── database.db  


## Como Executar

É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).


## Instalação das Dependências (no diretório backend):

Será necessário ter todas as bibliotecas Python listadas no `requirements.txt` instaladas. Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```sh
(env)$ pip install -r requirements.txt
```
Este comando instala as dependências/bibliotecas descritas no arquivo requirements.txt.


## Executando a API
Para executar a API, utilize:
``` sh
(env)$ python -m backend.app
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte.

``` sh(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra http://localhost:5000/swagger no navegador para verificar a documentação da API em execução.


## Estrutura do Banco de Dados

A tabela Tarefa possui os seguintes campos:

*id: Integer, Primary Key*

*titulo: String, Not Null*

*descricao: String*

*prazo: DateTime, Not Null*


## Frontend

O frontend consiste em um formulário para adicionar tarefas e uma tabela para listar, editar e excluir tarefas. 

## Endpoints da API

**/cadastrar_tarefa**  
Método: POST  
Descrição: Cadastra uma nova tarefa.  

**/buscar_tarefas**  
Método: GET  
Descrição: Busca todas as tarefas cadastradas.  

**/editar_tarefa/<id>**  
Método: PUT  
Descrição: Edita uma tarefa existente com base no ID.  

**/deletar_tarefa/<id>**  
Método: DELETE  
Descrição: Deleta uma tarefa existente com base no ID.  


## Documentação
Para acessar a documentação interativa da API com Swagger, abra o seguinte URL após iniciar o servidor Flask:

http://127.0.0.1:5000/swagger

