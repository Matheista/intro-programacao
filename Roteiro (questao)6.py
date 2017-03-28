i="sim"
while i == "sim":
    n1 = int(input("primeiro número: "))
    n2 = int(input("primeiro número: "))    
    if n1 > 0 and n2 > 0:
        soma=n1+n2
        print(soma)
        produto=n1*n2
        print(produto)
    else:
        media=((n1+n2)/2)
        print(media)

    i = str.lower(input("Gostaria de fazer uma nova execução? (sim ou não)"))
    
       
        
        

