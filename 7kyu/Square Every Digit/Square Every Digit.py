def square_digits(num):
    res = list(str(num))
    result = []
    # iterasi dengan mengkuadratkan setiap anggota list
    for i in res:
        result.append(int(i)**2)

    for i in result: 
        print(i, end="") 


square_digits(9119)