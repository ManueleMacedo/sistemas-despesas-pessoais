import json
import os
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'database', 'despesas.json')

def carregar_despesas():
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as file:
            return json.load(file)
    return []

def salvar_despesas(despesas):
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)
    with open(arquivo, 'w') as file:
        json.dump(despesas, file, indent=4)

def menu():
    os.system('cls')
    print('''

██████╗░███████╗░██████╗██████╗░███████╗░██████╗░█████╗░░██████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
██║░░██║█████╗░░╚█████╗░██████╔╝█████╗░░╚█████╗░███████║╚█████╗░
██║░░██║██╔══╝░░░╚═══██╗██╔═══╝░██╔══╝░░░╚═══██╗██╔══██║░╚═══██╗
██████╔╝███████╗██████╔╝██║░░░░░███████╗██████╔╝██║░░██║██████╔╝
╚═════╝░╚══════╝╚═════╝░╚═╝░░░░░╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░

██████╗░███████╗░██████╗░██████╗░█████╗░░█████╗░██╗░██████╗
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██║██╔════╝
██████╔╝█████╗░░╚█████╗░╚█████╗░██║░░██║███████║██║╚█████╗░
██╔═══╝░██╔══╝░░░╚═══██╗░╚═══██╗██║░░██║██╔══██║██║░╚═══██╗
██║░░░░░███████╗██████╔╝██████╔╝╚█████╔╝██║░░██║██║██████╔╝
╚═╝░░░░░╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═════╝░
''')
    print('''
            [1] - Adicionar despesa
            [2] - Buscar despesa (categoria | data)
            [3] - Editar despesa (categoria | data)
            [4] - Excluir despesa
            [5] - Relatório
            [6] - Sair
''')
    
def voltar_inicio():
    input('\nPressione qualquer tecla para voltar para o menu inicial: ')
    os.system('cls')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-'*(len(texto))
    print(linha)
    print(texto)
    print(linha)

    
def adicionar_despesa():
    lista_despesa = carregar_despesas()
    exibir_subtitulo('Adicionando Despesa')
    print('obs: sem letras maiúsculas, acentos e caracteres especiais')
    categoria = input('Qual é a categoria da sua despesa? - ')
    data = (input('Qual a data da despesa? (ex: 00/00/0000) - '))
    valor = float(input('Qual o valor da despesa? - '))

    lista_despesa.append({'categoria': categoria, 'data': data, 'valor': valor})
    salvar_despesas(lista_despesa)

    print('\nDespesa adicionada com sucesso!')
    voltar_inicio()
    

def buscar_despesa():
    lista_despesa = carregar_despesas()
    exibir_subtitulo('Buscar Despesa')
    buscando_despesa = input('Digite a categoria ou data da despesa: - ')

    busca = [
        despesa for despesa in lista_despesa
        if despesa['categoria'].lower() == buscando_despesa or despesa['data'].lower() == buscando_despesa.lower()
    ]

    if busca:
        print('\n')
        print(f'{'Categoria'.ljust(22)} |{' Data'.ljust(20)}  |{' Valor'.ljust(20)} \n')
        for despesa in busca:
            print(f"- {despesa['categoria'].ljust(20)} | {despesa['data'].ljust(20)} | {despesa['valor']:.2f}".ljust(20))
    else:
        print('Nenhuma despesa encontrada')

    voltar_inicio()
    
    

    
def tela_inicial():
    while True:
        menu()
        escolha = int(input('Qual opção você deseja? '))

        match escolha:
            case 1:
                adicionar_despesa()
            case 2:
                buscar_despesa()
            case 3:
                break
            case 4:
                break
            case 5:
                break
            case 6:
                break
            case _:
                break
            