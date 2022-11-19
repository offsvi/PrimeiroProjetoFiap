'''
Um equipamento com um determinado número serial foi danificado e será descartado. Precisamos eliminar
esse equipamento. Dica: para eliminar um item de uma lista, você utilizará o comando "del". Exemplo: del
'''
serial=int(input("Digite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
  if seriais[indice]==serial:
    del departamentos[indice]
    del equipamentos[indice]
    del seriais[indice]
    del valores[indice]
    break

for indice in range(0,len(equipamentos)):
  print("
Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])
