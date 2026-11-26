with open("mapa.txt","r",encoding="UTF-8") as f:
    najwieksza = None
    miasto = 0
    najwieksze_miasto = 0
    for line in f:
        line = line.strip()
        if(line == ''):continue
        line = line.split(" ")
        miasto += 1
        if(najwieksza == None or najwieksza < int(line[2])):
            najwieksza = int(line[2])
            najwieksze_miasto = miasto
            

print(najwieksze_miasto, najwieksza)

with open("wyniki4.txt","a",encoding="UTF-8") as t:
    t.write(f"4.1 {najwieksze_miasto} {najwieksza}")