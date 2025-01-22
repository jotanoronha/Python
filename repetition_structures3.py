v = int(input("Digite um valor: "))

# to  use the even version
if v % 2 == 1:
    v = (v - 1)

    for i in range(v,-1,-2):
        print(i)

else :
    for i in range(0,v,2):
        v = (v + 1)
        print(i)