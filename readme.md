# Aniver Lembre

## Descrição do Projeto
Este projeto é uma aplicação para gerenciamento de aniversários, permitindo que os usuários registrem e lembrem-se das datas de aniversário de amigos e familiares.

## Funcionalidades
- Cadastro de usuários
- Registro de aniversários
- Notificações de lembretes de aniversários (em andamento)

## Estrutura do Projeto
- **accounts/**: Gerencia a autenticação e perfis de usuários.
- **contacts/**: Armazena informações sobre os contatos e seus aniversários.
- **dashboard/**: Painel principal da aplicação.
- **reminders/**: Gerencia os lembretes de aniversários.
- **core/**: Contém configurações principais e arquivos de inicialização.

## Tecnologias Utilizadas
- Python
- Django
- SQLite
- HTML/CSS

## Como Executar o Projeto
1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Execute as migrações com `python manage.py migrate`.
4. Inicie o servidor com `python manage.py runserver`.