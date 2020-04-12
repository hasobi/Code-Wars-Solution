def squareDigits(num):
    # ubah num yang integer menjadi list of string
    res = list(str(num))
    
    # iterasi dengan mengkuadratkan setiap anggota list
    for i in res:
        print(int(i)**2, end="")