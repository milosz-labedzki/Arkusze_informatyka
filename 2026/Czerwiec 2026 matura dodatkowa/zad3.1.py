with open("dane.txt","r",encoding="UTF-8") as f:
    licznik = 0
    para = ""
    for line in f:
        line = line.strip()
        if(line == ''):continue
        for i in range(0,len(line),2):
            if(para == (line[i]+line[i+1])):licznik += 1
            para = line[i]+line[i+1]
            

with open("wyniki3.txt","w",encoding="UTF-8") as t:
    t.write(f"3.1 {licznik}")