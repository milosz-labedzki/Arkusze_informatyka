def podobna(n,T):
    k = n - 1
    for i in range(k,-1,-1):
        ok = True
        for j in range(0,i):
            if(T[j] != T[n-i+j]):
                ok = False
        if(ok == True):
            return i
    


print(podobna(10,[1,2,3,6,2,1,2,3,1,2]))
    