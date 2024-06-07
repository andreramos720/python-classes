texto= "curso de python"

print("#################### ANALISE DE STRING ##################")
print(texto)
print(texto [9:15:2]) #imprimir de 9 a 15 pulando de 2 em 2 "pto"
print(texto[:5]) #imprimir de 0 a 5 caractere "curso"
print(texto[9:]) #imprime da posição 9 em diante(python)
print(texto[6:8]) #imprime os caracteres "de"
print(len(texto)) #comando lenght 15 informa o tamanho da string
print(f"letras o:{texto.count('o')}") #informa a quantidade de letras
print(f"existe python?:{texto.find('python')}") #informa onde começa os caracteres(9) com espaço antes de python (8) e espaço depois de python(-1) que é não existe
print(f"python "in texto) #verifica se existe a palavra no texto retornando false or true

print("#################### TRANSFORMAÇÃO DE STRING ##################")

trocatexto=texto.replace("python","javascript") #substitui a string por alguma outra desejada
print(trocatexto)

semEspacotexto=texto.replace(" ","") #Tirar espaços do texto
print(semEspacotexto)

print(f"temos {texto} e {trocatexto} venha estudar no SENAI")

textoMinusculo=texto.lower() #transformar string em minusculo
print(textoMinusculo)

textoMaiusculo=texto.upper()  #transformar string em maiusculo
print(textoMaiusculo)

textoSemEspaco=texto.strip () #tira os espaços do começo e do final obs para direita rstrip e para apenas a esquerda lstrip
print(textoSemEspaco)

juntaTexto=''.join(texto)
print(juntaTexto)

divideTexto=''.split(texto)
print(divideTexto)






