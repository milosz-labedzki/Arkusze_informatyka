palindromy = []
dlugosc_aktualna = 0
liczba = 0
with open("wyrazy.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        slowo = line[0]
        palindrom = slowo[::-1]
        if(slowo == palindrom):
            palindromy.append(slowo)
            liczba +=1
            if(len(palindrom)>dlugosc_aktualna):
                dlugosc_aktualna = len(palindrom)
                najdluzszy = palindrom
print(f"{palindromy}, najdluzszy palindrom to: {najdluzszy} a liczba wierszy w ktorych jest palindrom to: {liczba}")