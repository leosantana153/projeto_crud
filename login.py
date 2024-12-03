
import PySimpleGUI as sg
from telas.menu import tela_menu

def tela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuário'), sg.Input(key='usuario')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
        [sg.Button('Entrar')]
    ]

    janela = sg.Window('Tela de Login', layout)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Entrar':
            if valores['usuario'] == 'leonardo' and valores['senha'] == '123456':
                sg.popup('Login bem-sucedido!')
                janela.close()
                tela_menu()
            else:
                sg.popup('Usuário ou senha incorretos!')

    janela.close()
