#1. Escreva uma função testaVogal que receba por parâmetro um caractere e retorne verdadeiro se
#ele for uma vogal, ou falso caso contrário.

"""def testaVogal(n):   
    if n == "a"or n == "e" or n == "i" or n == "o"or n == "u":
        return True
    else:
        return False
    
z=testaVogal(n=str.lower(input("Qual Letra? ")))
print(z)"""



#2. Escreva uma função calculaMaior que receba por parâmetro dois números e retorne o maior
#deles.
def calculaMaior(x,y):
    if x>=y:
        return x
    else:
        return y

"""z=calculaMaior(x=int(input("Qual o primeiro valor?")),y=int(input("Qual o segundo  valor?")))

print(z)"""

#3. Escreva uma função testaMultiplo4 que receba por parâmetro um número inteiro e retorne
#verdadeiro se ele for múltiplo de 4, ou falso caso contrário.

def testaMultiplo4(p):
    if p%4==0:
        return True
    else:
        return False

"""z=testaMultiplo4(int(input("Qual número? ")))
print(z)"""

#4. Escreva uma função testaDivisor que receba como parâmetro dois números inteiros, e retorne
#verdadeiro caso o segundo seja divisor do primeiro, ou falso caso contrário.

def testaDivisor(x,y):
    if x%y==0:
        return True
    else:
         return False
"""z=testaDivisor(int(input("Qual o primeiro número? ")),int(input("Qual segundo número? ")))

print(z)"""

#5. Escreva um programa para receber como entrada 20 números informados pelo usuário e,
#usando as funções testaMultiplo4 e testaDivisor já criadas, exibir a quantidade de múltiplos de 4
# e a soma dos divisores de 300 entre eles. 

"""QntM4=0
SmD300=0
for i in range(20):
    n=int(input("Qual o número? "))
    n1=testaMultiplo4(n)
    if n1 == True:
        QntM4+=1
    n2=testaDivisor(300,n)
    if n2 == True:
        SmD300+=n
        
print(QntM4)
print(SmD300)"""

#6Escreva um programa para receber como entrada 50 números informados pelo usuário e exibir
#o maior deles, utilizando a função calculaMaior já criada.

"""maior=0
for i in range(50):
    n=int(input("Qual o número?"))    
    z=calculaMaior(maior,n)
    if z == n:
        maior=n
        
print(maior)"""
