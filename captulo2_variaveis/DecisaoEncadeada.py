# INICIO DO PROGRAMA
nome = input("Digite o nome: ")
idade = int(input("digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NÃO":
        print("Encaminhe o ppaciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NÃO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
