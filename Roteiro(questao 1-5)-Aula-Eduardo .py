i = 3
while i > 0:
    n1 = int(input("primeiro número: "))
    n2 = int(input("primeiro número: "))

    if n1 > 0 and n2 > 0:
        soma=n1+n2
        print(soma)
        produto=n1*n2
        print(produto)
    else:
        media=(n1+n2/2)
        print(media)

    i-= 1
