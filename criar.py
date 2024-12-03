
import PySimpleGUI as sg
from database.conexao import conectar

def tela_criar():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome'), sg.Input(key='nome')],
        [sg.Text('CPF'), sg.Input(key='cpf')],
        [sg.Text('Data de Cadastro (YYYY-MM-DD)'), sg.Input(key='data_cadastro')],
        [sg.Text('Data de Nascimento (YYYY-MM-DD)'), sg.Input(key='data_nascimento')],
        [sg.Text('E-mail'), sg.Input(key='email')],
        [sg.Button('Salvar'), sg.Button('Voltar')]
    ]

    janela = sg.Window('Criar Cliente', layout)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar':
            break
        if eventos == 'Salvar':
            conexao = conectar()
            cursor = conexao.cursor()
            sql = "INSERT INTO clientes (nome, cpf, data_cadastro, data_nascimento, email) VALUES (%s, %s, %s, %s, %s)"
            valores_sql = (
                valores['nome'], valores['cpf'], valores['data_cadastro'],
                valores['data_nascimento'], valores['email']
            )
            cursor.execute(sql, valores_sql)
            conexao.commit()
            cursor.close()
            conexao.close()
            sg.popup('Cliente cadastrado com sucesso!')
            janela.close()

    janela.close()
