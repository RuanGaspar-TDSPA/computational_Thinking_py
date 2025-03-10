import json 
# Lê arquivo json e retorna lista de pacientes
def carrega_pacientes():

    with open("pacientes.json") as arquivo:
        pacientes = json.load(arquivo)
    return pacientes

# Recebe lista de pacientes e exibe apenas o seus nomes
def mostra_nomes(pacientes: list):
    for paciente in pacientes:
        print(paciente["nome"])

def main():
    pacientes = carrega_pacientes()
    mostra_nomes(pacientes)
    dados_pacientes(pacientes)

'''Exercício: escreva a função que recebe lista de pacientes e 
printa todas as informações (nome, idade, id)'''

def le_novo_paciente():
    pacciente = {} #Dicionário começa vazio

    print("Informe o nome do paciente:")
    nome = input()
    paciente["nome"] = nome
    """Execício: ler idade e ID interno e colocar nos respectivos campos do dicionário"""
print("Informe nome do paciente")
nome = input()
paciente["nome"] = nome

print("Informe idade do paciente")
idade = int(input())
paciente["idade"] = idade

print("Informe id do paciente")
idade = int(input())
paciente["id"] = id

def main():

    while em_execucao:

        opcao = int(input())
        if opcao == 0:
            em_execucao





def dados_pacientes(pacientes: list):
        for paciente in pacientes:
            print(f"Paciente {nome}, {idade} anos, identificação número {id}")

#Outro exemplo
def main():
    pacientes = carrega_pacientes()
    em_execucao = True 
    while em_execucao:
        print("Escolha uma opção")
        print("0. Sair do programa")
        print("1. Mostrar pacientes")

        opcao = int(input())
        if opcao == 0:
            em_execucao = False
        elif opcao == 1:
            dados_pacientes(pacientes)
        print("Encerrrando o programa")
   
'''nomes_pacientes = []
for paciente in pacientes:
    nomes_pacientes.append(paciente["nome"])

print(nomes_pacientes)
print(pacientes)'''