# CRUD de Clientes - Sistema de Cadastro

Este projeto é um sistema simples de CRUD (Criar, Ler, Atualizar, Deletar) para o gerenciamento de clientes. Ele foi desenvolvido com a biblioteca **PySimpleGUI** para a interface gráfica e o **MySQL** para o banco de dados.

## Funcionalidades

- **Criar**: Adicionar novos clientes ao banco de dados.
- **Listar**: Visualizar todos os clientes cadastrados.
- **Atualizar**: Editar os dados de um cliente existente.
- **Deletar**: Remover um cliente do banco de dados.

## Tecnologias Usadas

- **Python**: Linguagem principal do projeto.
- **PySimpleGUI**: Biblioteca para a criação da interface gráfica.
- **MySQL**: Banco de dados para armazenar as informações dos clientes.

## Pré-requisitos

- Ter o **Python 3** instalado.
- Ter o **MySQL** instalado e configurado.
- Ter o **PySimpleGUI** e o **mysql-connector** instalados no ambiente Python.

## Instalação

1. Clone este repositório no seu computador:
    ```bash
    git clone https://github.com/seunome/seu-repositorio.git
    ```
2. Acesse a pasta do projeto:
    ```bash
    cd seu-repositorio
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - **Linux/macOS**:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```

6. Configure o banco de dados MySQL com a tabela **clientes**.

## Como Usar

1. Execute o script principal:
    ```bash
    python main.py
    ```
2. O sistema de cadastro de clientes será aberto.
3. Utilize a interface para adicionar, listar, atualizar e deletar clientes.

## Estrutura do Projeto

meu_projeto/ ├── database/ │ ├── init.py │ └── conexao.py ├── telas/ │ ├── init.py │ ├── criar.py │ ├── listar.py │ ├── login.py │ └── menu.py ├── init.py ├── main.py ├── requirements.txt └── README.md


## Contribuindo

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Para isso, basta fazer um **fork** do repositório, realizar as alterações e abrir um **pull request**.

## Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

