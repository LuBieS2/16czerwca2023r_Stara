a=17
b=431
def digits(a):
    a=str(a)
    al=[]
    for i in a:
        al.append(int(i))
    return al
def czy_przyjaciółki(a, b):
    a=digits(a)
    b=digits(b)
    sa=0
    sb=0
    for i in a:
        sa+=i
    for i in b:
        sb+=i
    if sb==sa:
        return True
    return False
def czy_dobre():
    x=digits(a)
    y=digits(b)
    if czy_przyjaciółki(a, b):
        if x[0]==y[-1] or x[-1]==y[0]:
            return True
    return False
print(czy_przyjaciółki(a,b), czy_dobre())