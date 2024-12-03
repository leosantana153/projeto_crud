
import PySimpleGUI as sg
from telas.criar import tela_criar
from telas.listar import tela_listar

def tela_menu():
    sg.theme('Reddit')
    layout = [
        [sg.Button('Criar Cliente')],
        [sg.Button('Listar Clientes')],
        [sg.Button('Sair')]
    ]

    janela = sg.Window('Menu Principal', layout)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Sair':
            break
        if eventos == 'Criar Cliente':
            janela.close()
            tela_criar()
        if eventos == 'Listar Clientes':
            janela.close()
            tela_listar()

    janela.close()
