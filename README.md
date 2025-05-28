# Sistema de Estoque (Python + MySQL)

Este é um sistema simples de gerenciamento de estoque utilizando **Python** e **MySQL**. Ele permite realizar operações CRUD (Create, Read, Update e Delete) em um banco de dados de produtos via terminal.

## Funcionalidades

- [x] Adicionar novo produto ao banco de dados
- [x] Visualizar todos os produtos cadastrados
- [x] Atualizar nome ou preço de produtos
- [x] Deletar produtos do banco de dados por ID
- [x] Interface simples via terminal

## Tecnologias utilizadas

- Python 3.x
- MySQL Server
- Biblioteca `mysql-connector-python` (oficial da Oracle)

## Pré-requisitos

- Ter o **MySQL Server** instalado e em execução
- Ter criado o banco de dados e a tabela com o seguinte comando:

  SQL
    CREATE DATABASE estoque;
    
    USE estoque;
    
    CREATE TABLE produtos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        preço FLOAT
    );
  
  ## Instalar a biblioteca necessária no Python:
    pip install mysql-connector-python
  
## Como executar

1. Atualize os dados de conexão no script
No trecho abaixo do arquivo sistema_de_estoque(MySQL).py, altere se necessário!

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sua_senha",
    database = "estoque"
)

2. Execute o script
   python sistema_de_estoque(MySQL).py

3. Siga as opções do menu
  [0] Para sair do programa.
  [1] Adicionar novo produto.
  [2] Ver o estoque.
  [3] Modificar dados do estoque.
  [4] Deletar coluna do estoque

## Observações
O campo preço usa o tipo FLOAT. Para sistemas maiores, pode-se considerar o uso de DECIMAL com precisão.

A opção [4] (Deletar) remove o produto com base no ID.

A senha e usuário do MySQL estão em texto no código. Para produção, use variáveis de ambiente ou arquivos .env.
