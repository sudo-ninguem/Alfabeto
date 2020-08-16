nomes = []
saida = "s"

while(saida == "s"):
  nomes.append(input ("Digite um nome: "))
  
  saida = input ("Se deseja acrescentar mais um nome digite (s) se não digite qualquer outra coisa: ")


nomes.sort()

print (nomes)
