def czy_pierwsza(n):
    if(n<2): return False
    pierwiastek = int(n ** 0.5)
    for i in range(2,pierwiastek+1):
        if(n % i == 0): return False
    return True





with open("dane.txt","r",encoding="UTF-8") as f:
    para = ""
    napis = ""
    najlepszy = ""
    for line in f:
        line = line.strip()
        for i in range(0,len(line),2):
            wartosc = 0
            for j in range(i,len(line)-1,2):


                para = line[j]+line[j+1]
                wartosc += ord(line[j]) + ord(line[j+1])
                pierwsza = czy_pierwsza(wartosc)


                if(pierwsza == True):
                    napis = line[i:j+2]
                    if(len(najlepszy) < len(napis)): najlepszy = napis


with open("wyniki3.txt","a",encoding="UTF-8") as t:
    t.write(f"\n3.2 {najlepszy}")
                    