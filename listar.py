import PySimpleGUI as sg
from database.conexao import conectar

def tela_listar():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conexao.close()

    layout = [[sg.Text('Lista de Clientes')]]

    for cliente in clientes:
        layout.append([
            sg.Text(str(cliente)),
            sg.Button('Deletar', key=f'deletar_{cliente[0]}')
        ])

    layout.append([sg.Button('Voltar')])

    janela = sg.Window('Listar Clientes', layout)

    while True:
        eventos, valores = janela.read()

        if eventos == sg.WIN_CLOSED or eventos == 'Voltar':
            break

        if eventos.startswith('deletar_'):
            id_cliente = eventos.split('_')[1]
            confirmar_delecao(id_cliente)

    janela.close()

def confirmar_delecao(id_cliente):
    layout_confirmacao = [
        [sg.Text(f"Tem certeza que deseja excluir o cliente com ID {id_cliente}?")],
        [sg.Button('Sim'), sg.Button('Não')]
    ]
    janela_confirmacao = sg.Window('Confirmar Exclusão', layout_confirmacao)

    while True:
        eventos, valores = janela_confirmacao.read()
        
        if eventos == sg.WIN_CLOSED or eventos == 'Não':
            janela_confirmacao.close()
            break
        
        if eventos == 'Sim':
            excluir_cliente(id_cliente)
            janela_confirmacao.close()
            break

def excluir_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(f"DELETE FROM clientes WHERE id = {id_cliente}")
    conexao.commit()
    cursor.close()
    conexao.close()

    sg.popup('Cliente excluído com sucesso!')

