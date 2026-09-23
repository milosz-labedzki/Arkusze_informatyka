lista = []
zliczenia = 0
palindromy = []
with open("hasla.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        slowo = sorted(line)
        for i in slowo:
            for j in slowo[i]:
                if(slowo[i] == slowo[j]):
                    print(slowo[i])
