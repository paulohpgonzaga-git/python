import random

#biblioteca randmom, lista, arquivo, método escrita, leitura e adicionar, repetição, interpolacao

arquivo = open("arquivo_qualquer.txt","w") #write

x=0
for x in range(20):
    arquivo.write(str(random.randrange(0,20))+"\n")

arquivo.close()

arquivo = open("arquivo_qualquer.txt","r") #read

lista =[]
index = 0
for linha in arquivo:
    linha = linha.strip()
    lista.append(linha)
    index = index + 1

print("Conteudo do Arquivo ->{}".format(lista))
print("Quantidade de elementos ->{}".format(index))
print("\nMaior valor ->"+max(lista))
print("\nMenor valor ->"+min(lista))

  
arquivo = open("arquivo_qualquer.txt","a") #add  
arquivo.write("FIM do arquivo\n")
arquivo.close()