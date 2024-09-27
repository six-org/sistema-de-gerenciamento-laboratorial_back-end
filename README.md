# Gerenciamento Laboratorial

**Descrição**:  
O *Gerenciamento Laboratorial* é um sistema de gerenciamento de laboratórios clínicos. Nosso objetivo é facilitar a administração de laboratórios, otimizando operações e melhorando a eficiência por meio de uma plataforma integrada e acessível.

## Requisitos

- Python 3.8+
- Django 4.x
- Django REST Framework
- PostgreSQL 16
- Git

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/gerenciamento_laboratorial.git
    cd sistema-de-gerenciamento-laboratorial_back-end/gerenciamento_laboratorial
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements/base.txt
    ```

4. Configure o banco de dados PostgreSQL:

    Certifique-se de que o PostgreSQL esteja rodando e crie o banco de dados:

    ```sql
    CREATE DATABASE gerenciamento_laboratorial;
    ```

    Configure as credenciais no arquivo `.env`:

    ```bash
    DATABASE_URL=postgres://<usuario>:<senha>@localhost:5432/gerenciamento_laboratorial
    ```

5. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

    Acesse o sistema em [http://localhost:8000](http://localhost:8000).
