lista = []
zliczenia = 0
palindromy = []
with open("hasla.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        slowo = line[::-1]
        if(line == slowo):
            palindromy.append(line)
            zliczenia += 1

print(f"palindromy to{palindromy} a ich liczba to {zliczenia}")