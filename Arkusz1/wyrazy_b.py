zliczenia = {}
slowa = []
liczba = 0
najwiecej = 0
with open("wyrazy.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        slowo = line[0]
        if(slowo not in slowa):
            slowa.append(slowo)
            liczba += 1
        zliczenia[slowo] = zliczenia.get(slowo,0) + 1
        if(najwiecej < zliczenia[slowo]):
            najwiecej = zliczenia[slowo]
        if(zliczenia[slowo] == 9):
            najczestsze_slowo = slowo
print(liczba)
print(najczestsze_slowo,najwiecej)
