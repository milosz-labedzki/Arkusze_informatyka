lista = []
lista_anagramow = []
with open("wyrazy.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        slowo = line[0]
        lista.append(slowo)  
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if(sorted(lista[i])==sorted(lista[j])):
                    lista_anagramow.append((lista[i],lista[j]))
    lista_anagramow = set(lista_anagramow)
print(print(lista_anagramow))