## API de Clientes
![Static Badge](https://img.shields.io/badge/Status-Finalizado-green)

API REST desenvolvida com Django REST Framework para gerenciamento de dados de clientes. O projeto foi desenvolvido como parte do curso de Django REST Framework da Alura.

## Tecnologias Utilizadas

* Python
* Django
* Django REST Framework
* Django Filters
* Django REST Framework Simple Pagination

## Descrição Detalhada

Esta API fornece um conjunto de endpoints para interagir com dados de clientes. A API implementa as seguintes funcionalidades:

**Funcionalidades Principais:**

* **CRUD completo de clientes:** Crie, visualize, atualize e exclua registros de clientes.
* **Validações Personalizadas:** Garante a integridade dos dados com validações personalizadas implementadas nos models e serializers.
* **Filtragem de Dados:** Filtre clientes por nome, status ativo/inativo utilizando Django Filters.
* **Ordenação de Dados:** Ordene os resultados da consulta por nome.
* **Paginação:** Permite a paginação dos resultados da consulta para melhor performance com grandes conjuntos de dados, utilizando Django REST Framework Simple Pagination.
* **Barra de Pesquisa:** Permite a pesquisa de clientes pelo nome.

**Como Executar o Projeto Localmente:**

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/django-rest-clientes.git
   ```
2. Crie um ambiente virtual e ative-o:
   ```bash
   poetry install
   poetry shell
   ```
3. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```
4. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

**Considerações:**

Este projeto foi desenvolvido para fins de aprendizado durante o curso da Alura e pode ser utilizado como base para projetos similares. 
