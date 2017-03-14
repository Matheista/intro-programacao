#1.1
"""cont = 20#<=faltou colocar o "soma=0" fora do while
while (cont > 0):
    numero = int (input())#<=isso tem que ser fora do while
    if (numero % 2):#<= faltou o "==0"
    soma = numero#<= faltou o "+="
    cont = cont + 1#<= contador tem que ser -1
    
print(soma)"""

#Corrigido
"""cont = 5
soma = 0
while cont > 0:
    numero = int(input("informe número: "))
    if numero % 2== 0:
        soma += numero
    cont-=1

print(soma)"""

#1.2

"""cont = 0
qtdePositivos = 0
numero = int (input())#<= isso deveria ser informado  dentro do while
while (cont > 0):#<= aqui o cont deveria estar (cont<30)
    if (numero >= 0):
        qtdePositivos = numero + 1#<=aqui deveria ter somente "+=" e não numero +1
    cont = cont + 1 #<=aqui deveria ser "+=" e não +1
print(cont)#<=aqui deveria exibir "qtdePositivos" e não cont

"""
#Corrigido
"""cont=0
qtdePositivos = 0
while cont <5:
    numero = int(input("informe número: "))
    if numero >=0:
        qtdePositivos+=1
    cont+=1
print(qtdePositivos)"""

#2

"""Escreva um programa que receba como entrada 25 números e exiba a quantidade de
números que são pares e positivos."""

"""cont =5
QtdePosPar=0

while cont>0:
    numero=int(input("informe número: "))
    if numero >0 and numero %2==0:
        QtdePosPar+=1
    cont-=1
print(QtdePosPar)"""



#4


"""num=int(input("informe numero: "))
soma = 0
Qtde=0
while num!=100:
    if num % 2 ==0:
        soma+=num
        Qtde+=1
    num=int(input("informe numero: "))
    if num % 2 !=0:
        print("errado")
print("Média",soma//Qtde)"""




#5

"""r="s"
quant = 0
while r =="s":
    idade=int(input("informe idade da criança: "))
    if idade >=3 and idade <=5:
        quant+=1
    r = str.lower(input("Gostaria de fazer uma nova execução? (s/n)"))

print(quant)"""




"""#6

filho=0
cont=0
soma=0
while filho >= 0:
    filho=int(input("Quantos filhos você possui?"))
    if filho >= 0:
        soma+=filho
        print(soma)
        cont+=1
        print(cont)
print("Média",soma//cont)"""
        
    


















