<h1 align="center">
  Web browsable API <br> SpaceX Consumer
</h1>

Elaborar uma API em Python/Django com front-end que consuma a API da SpaceX e seja capaz de apresentar as seguintes informações:

- Próximo Lançamento
- Último Lançamento
- Próximos Lançamentos
- Lançamentos Passados

## 👨🏼‍💻 Desenvolvedor

- [Paulo Henrique Bernardes Martins](http://phdeveloper.com.br/)

## 🚀 Tecnologias

- ⚡ [Django](https://www.djangoproject.com/) — A web framework for Python.
- 💾 [Django REST framework](https://www.django-rest-framework.org/) — Toolkit Web APIs for Python.

## ✋🏻 Pré-requisitos

- [Python](https://www.python.org/)

## 🔥 Instalação e execução

1. Faça um clone desse repositório;
2. Entre na pasta `cd ApiSpaceXConsumer`;
3. Rode `python -m venv venv` para criar a Virtual Environment;
4. Rode `\env\Scripts\activate` para ativar a Virtual Environment;
5. Rode `pip install requirements-dev.txt` para instalar as dependências;
6. Rode `python manage.py migrate` para fazer as migrações;
8. Rode `python manage.py createsuperuser` escolha um nome de usuário e senha;
7. Rode `python manage.py runserver` para subir o servidor de desenvolvimento;

## 📚 Implementação

Eu criei um projeto django chamado ApiSpaceXConsumer onde ficam as configurações básica do projeto:
`Pasta => ApiSpaceXConsumer `
- `urls.py`
- `settings.py`

Em seguida eu inicio um app django chamado `api` onde se encontra a regra de negocio da api consumer:

`Pasta => api `
- `admin.py` 
- `models.py`

Na pasta `core` encontramos os arquivo utilizado pelo Django Rest Framework onde exponho a api

`Pasta => api => core`
- `serializers.py` 
- `viewsets.py`

---