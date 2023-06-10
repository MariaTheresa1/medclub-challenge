# Medclub Challenge
### Este projeto é uma API RESTful que utiliza (Django REST framework)[https://www.django-rest-framework.org/] e gerencia usuários, itens e pedidos.

## Configuração do ambiente (Windows)
### Instale o Python
Faça o download da versão do Python 3.11.3 [aqui](https://www.python.org/downloads/).
### Configure o virtualenv e instale o Django
### Crie o ambiente virtual
```
python -m venv venv
```
### Ative o ambiente virtual
```
venv\Scripts\Activate
```
### Instale as dependências
```
pip install -r requirements.txt
```
### Executa o projeto localmente em [localhost](http://127.0.0.1:8000/users/)
```
python manage.py runserver
```

## Documentação da API

### Instale o Postman [aqui](https://www.postman.com/downloads/), ele será usado para testar a API.

#### <center>Cadastrar um usuário</center>
#### Não precisa estar autenticado.
http://127.0.0.1:8000/users/
### POST
```
{
    "username": "pedro",
    "password": "1111"
}
```
Resposta 201:
```
{
    "id": 9,
    "username": "pedro",
    "first_name": "",
    "last_name": "",
    "email": ""
}
```

#### Gerar um token para um usuário cadastrado
http://127.0.0.1:8000/users/api-token-auth/
### POST
```
{
    "username": "maria",
    "password": "1234"
}
```
Resposta 201:
```
{
    "token": "ab19ec58be1233e610a7fd55859aa783b400555d"
}
```
Resposta 400:
```
{
    "non_field_errors": [
        "Impossível fazer login com as credenciais fornecidas."
    ]
}
```
Resposta 401:
```
{
    "detail": "Usuário ou senha inválido."
}
```

#### Recuperar, atualizar ou deletar um usuário (o usuário deve estar autenticado).
http://127.0.0.1:8000/users/1

##### Para realizar a autenticação pelo Postman:
* Fornecer Token no Headers ou
* Fornecer username e password em Authorization

### GET
Resposta 200:
```
{
    "id": 1,
    "username": "maria",
    "first_name": "",
    "last_name": "",
    "email": "mariatheresa98@hotmail.com",
}
```
### PUT, PATCH
```
{
    "username": "user222alterado",
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": 1234
}
```
Resposta 200:
```
{
    "username": "user222alterado",
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": 1234
}
```
### DELETE
```
{
    "id": 1
}

```
Resposta 200.

#### Observe que mesmo alterando o parâmetro <id> na URL o usuário autenticado só conseguirá retornar seus próprios dados. Se as credenciais não forem fornecidadas, retornará erro 401:
```
{
    "detail": "As credenciais de autenticação não foram fornecidas."
}
```
ou
```
{
    "detail": "Usuário ou senha inválido."
}
```

#### <center>Cadastrar Itens</center>
#### Não precisa estar autenticado.
http://127.0.0.1:8000/items/
### POST
```
{
    "name": "Leite 1L Piracanjuba",
    "price": "6.50"
}
```
Resposta 200:
```
{
    "id": 4,
    "name": "Leite 1L Piracanjuba",
    "price": "6.50"
}
```
#### Recuperar, atualizar ou deletar um item
http://127.0.0.1:8000/items/4/
### GET
Resposta 200:
```
{
    "id": 4,
    "name": "Leite 1L Piracanjuba",
    "price": "6.50"
}
```
### PUT, PATCH
```
{
    "name": "Leite Integral 1L Piracanjuba",
    "price": "6.50"
}
```
Resposta 200:
```
{
    "id": 4,
    "name": "Leite Integral 1L Piracanjuba",
    "price": "6.50"
}
```
### DELETE
```
{
    "id": 4
}
```
Resposta 200.

#### <center>Cadastrar Pedidos</center>
#### O usuário deve estar autenticado.
http://127.0.0.1:8000/orders/
### POST
```
{
    "items": [
        2,
        5,
        9
    ]
}
```
Resposta 200:
```
{
    "id": 4,
    "user": 1,
    "created_at": "2023-06-09T22:46:56.314749-03:00",
    "items": [
        2,
        5,
        9
    ]
}
```
#### Recuperar, atualizar ou deletar um item
http://127.0.0.1:8000/orders/3/
### GET
Resposta 200:
```
{
    "id": 3,
    "user": 1,
    "created_at": "2023-06-09T22:33:54.348731-03:00",
    "items": [
        6,
        7,
        8
    ]
}
```
### PUT, PATCH
```
{
  "items": [6, 7, 8]
}
```
Resposta 200:
```
{
    "id": 3,
    "user": 1,
    "created_at": "2023-06-09T22:33:54.348731-03:00",
    "items": [
        6,
        7,
        8
    ]
}
```
### DELETE
```
{
    "id": 3
}
```
Resposta 200.

Note que, caso o usuário não esteja autenticado, será retornado erro 401 Unauthorized: 
```
{
    "detail": "As credenciais de autenticação não foram fornecidas."
}
```
