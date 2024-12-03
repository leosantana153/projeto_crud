# Sistema de Cadastro de Clientes - Projeto Python

Este projeto utiliza **Python**, **PySimpleGUI** para a interface gráfica e **MySQL** para o banco de dados, permitindo o gerenciamento de clientes. Funcionalidades incluem cadastro, listagem, edição e exclusão de clientes, com autenticação via login.

## Funcionalidades

- **Cadastro de Clientes**: Adiciona novos clientes com informações como nome, CPF, e-mail, etc.
- **Listagem de Clientes**: Exibe todos os clientes cadastrados.
- **Edição de Clientes**: Permite editar informações de um cliente existente.
- **Exclusão de Clientes**: Permite excluir um cliente do banco de dados.

## Tecnologias Utilizadas

- **Python 3.x**
- **PySimpleGUI**
- **MySQL**

## Como Executar o Projeto

### Passo 1: Clonar o Repositório


git clone https://github.com/seu_usuario/meu_projeto.git
Passo 2: Criar e Ativar o Ambiente Virtual
bash
Copiar código
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate


Passo 3: Instalar Dependências
pip install -r requirements.txt


Passo 4: Configurar o Banco de Dados
Crie o banco de dados e a tabela:


CREATE DATABASE meu_projeto;
USE meu_projeto;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    data_cadastro DATE NOT NULL,
    data_nascimento DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Inserir dados de exemplo
INSERT INTO clientes (nome, cpf, data_cadastro, data_nascimento, email) VALUES
('João Silva', '123.456.789-00', '2022-05-28', '1990-06-15', 'joao.silva@email.com'),
...
Passo 5: Executar o Projeto

python main.py
Estrutura do Projeto
markdown
Copiar código
meu_projeto/
├── database/
│   ├── __init__.py
│   └── conexao.py
├── telas/
│   ├── __init__.py
│   ├── criar.py
│   ├── listar.py
│   ├── login.py
│   └── menu.py
├── __init__.py
├── main.py
├── requirements.txt
└── README.md
