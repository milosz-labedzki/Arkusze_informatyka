with open("dane.txt","r",encoding="UTF-8") as f:
    wyraz = 0
    for line in f:
        line.strip()
        zliczenia = {}
        for i in range(0,len(line)-1,2):
            para = line[i] + line[i+1]
            zliczenia[para] = zliczenia.get(para,0)+1
    wyraz = "".join(sorted(zliczenia, key=zliczenia.get))

with open("wyniki3.txt","a",encoding="UTF-8") as t:
    t.write(f"\n3.3 {wyraz}")        