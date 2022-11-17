nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa == "SIM":
    print("Enacmihe o paciente para sala AMARELA")
elif doenca_infectocontagiosa == "NAO":
    print("Encaminhe o paciente para sala BRANCA")
else:
    print("Responda a suspeita se doença infectocontagiosa com SIM ou NAO")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o genero do paciente: ").upper()
    if genero == "FEMININO" and idade >10:
        gravidez = input("A paciente está gravida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
