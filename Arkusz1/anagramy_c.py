lista = []
lista_anagramow = []
zliczenia = {}
with open("wyrazy.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        slowo = line[0]
        lista.append(slowo)
        klucz = "".join(sorted(slowo))

        if(klucz not in zliczenia):
            zliczenia[klucz] = []
        zliczenia[klucz].append(slowo)
        
            
print(zliczenia)

