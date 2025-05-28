import mysql.connector

# Estabelece a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "lima0409",
    database = "estoque"
)

cursor = conexao.cursor()

# Função que exibe o menu principal
def menu():
    print('''
    [0] Para sair do programa.
    [1] Adicionar novo produto.
    [2] Ver o estoque.
    [3] Modificar dados do estoque.
    [4] Deletar coluna do estoque''')

# Loop principal do programa
while True:
    menu()
    escolha = int(input('ESCOLHA:'))

    if escolha == 0:
        print('Volte sempre!')
        break

    elif escolha == 1:
        # CREATE - Adiciona novo produto
        adicionar_produto = input('Nome do produto:')
        preço = float(input('Preço:'))
        create_comando = 'INSERT INTO produtos(nome, preço) VALUES (%s, %s)'
        adicionar_valores = adicionar_produto, preço
        cursor.execute(create_comando, adicionar_valores)
        conexao.commit()
        print('Produto adicionado com sucesso!')
        continue

    elif escolha == 2:
        # READ - Lista todos os produtos do estoque
        comando = 'SELECT * FROM produtos'
        cursor.execute(comando)
        resultado_leitura = cursor.fetchall()
        for linha in resultado_leitura:
            id = linha[0]
            nome = linha[1]
            valor = linha[2]
            print(f'id: {id} -- Nome: {nome} -- Preço: {valor}R$')
        continue

    elif escolha == 3:
        # UPDATE - Modifica o nome ou preço de um produto
        endereco_coluna = input('Qual coluna será alterada? ("Nome", "Preço")').lower()
        id_coluna = int(input('Digite o ID da coluna que será alterada:'))

        if endereco_coluna == 'nome':
            novo_nome = input('NOVO NOME:')
            update_comando1 = 'UPDATE produtos SET nome = %s WHERE id = %s'
            valores_update1 = novo_nome, id_coluna
            cursor.execute(update_comando1, valores_update1)
            conexao.commit()
            print('Alteração feita com sucesso!')

        elif endereco_coluna == 'preço':
            novo_valor = input('NOVO PREÇO:')
            update_comando2 = 'UPDATE produtos SET preço = %s WHERE id = %s'
            valores_update2 = novo_valor, id_coluna
            cursor.execute(update_comando2, valores_update2)
            conexao.commit()
            print('Alteração feita com sucesso!')

        else:
            print('ENDEREÇO INVÁLIDO!')
        continue

    elif escolha == 4:
        # DELETE - Deleta um produto com base no ID
        delete_coluna = input('Digite o ID da coluna que será apagada:')
        valor_delete = (int(delete_coluna),)
        delete_comando = 'DELETE FROM produtos WHERE id = %s'
        cursor.execute(delete_comando, valor_delete)
        conexao.commit()
        print('Coluna deletada com sucesso!')
        continue

# Fecha a conexão
cursor.close()
conexao.close()
